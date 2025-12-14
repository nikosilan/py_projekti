from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
from aircraft_utils import GameState, Airport
from geopy.distance import geodesic


##############################################
# IMPORTOITU APP.PY TIEDOSTOON
##############################################


app = Flask(__name__)
CORS(app)

# Käyttäjäkohtaiset asetukset
USERS = {
    "niko": {"user": "niko", "password": "salasana"},
    "juuso": {"user": "Juuso", "password": "salasana"},
    "daniel": {"user": "Daniel", "password": "DA10"},
    "illia": {"user": "illia", "password": "salasana3"}
}

BASE_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "autocommit": True
}

# Hae satunnaiset lentokentät
@app.route("/api/random_destinations/<int:flights>")
def random_destinations(flights):
    username = request.args.get("username", "illia").lower()
    user_config = USERS.get(username, USERS["illia"])
    # Jos yhteys tietokantaan epäonnistuu
    try:
        conn = mysql.connector.connect(**BASE_CONFIG, **user_config)
    except Exception as e:
        print("MySQL error:", e)
        raise

    kohteet = GameState.random_destination(conn, flights)
    conn.close()
    return jsonify([
        {"icao": icao, "name": nimi, "country": maa, "lat": lat, "lon": lon}
        for icao, nimi, maa, lat, lon in kohteet
    ])

# Hae nykyinen sijainti
@app.route("/api/current_location")
def current_location():
    username = request.args.get("username", "illia").lower()
    user_config = USERS.get(username, USERS["illia"])
    conn = mysql.connector.connect(**BASE_CONFIG, **user_config)

    result = Airport.get_current_airport(conn)
    conn.close()

    if result:
        ident, name, country, lat, lon = result
        return jsonify({
            "icao": ident,
            "name": name,
            "country": country,
            "lat": lat,
            "lon": lon
        })
    else:
        return jsonify({"message": "Sijaintia ei löytynyt"}), 404

# Päivitä sijainti ja laske etäisyys
@app.route("/api/set_destination", methods=["POST"])
def set_destination():
    data = request.get_json()
    username = data.get("username", "illia").lower()
    new_icao = data.get("icao")

    if not new_icao:
        return jsonify({"success": False, "message": "ICAO puuttuu"}), 400

    user_config = USERS.get(username, USERS["illia"])
    conn = mysql.connector.connect(**BASE_CONFIG, **user_config)

    # Hae nykyinen sijainti
    current = Airport.get_current_airport(conn)
    # Hae valittu kohde
    new_airport = Airport.get_airport_info(new_icao, conn)

    if not current or not new_airport:
        conn.close()
        return jsonify({"success": False, "message": "Lentokenttätietoja ei löytynyt"}), 404

    # Lasketaan etäisyys
    distance = geodesic(
        (current[3], current[4]),
        (new_airport[3], new_airport[4])
    ).kilometers

    # Päivitä sijainti tietokantaan
    cursor = conn.cursor()
    sql = "UPDATE game SET sijainti = %s WHERE id = 1"
    cursor.execute(sql, (new_icao,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "success": True,
        "message": f"Sijainti päivitetty {new_icao}",
        "from": {
            "icao": current[0],
            "name": current[1]
        },
        "to": {
            "icao": new_airport[0],
            "name": new_airport[1]
        },
        "distance_km": distance
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)

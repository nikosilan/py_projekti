from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
from aircraft_utils import GameState

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

@app.route("/api/random_destinations/<int:flights>")
def random_destinations(flights):
    username = request.args.get("username", "niko").lower()
    user_config = USERS.get(username, USERS["niko"])
    conn = mysql.connector.connect(**BASE_CONFIG, **user_config)

    kohteet = GameState.random_destination(conn, flights)
    conn.close()
    return jsonify([
        {"icao": icao, "name": nimi, "country": maa, "lat": lat, "lon": lon}
        for icao, nimi, maa, lat, lon in kohteet
    ])

if __name__ == "__main__":
    app.run(port=5000, debug=True)

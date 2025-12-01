from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS
from aircraft_utils import GameState 

app = Flask(__name__)
CORS(app)

# MySQL-yhteys
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="niko",
    password="salasana",
    autocommit=True
)

# Endpoint palauttaa kolme satunnaista kohdetta JSONina
@app.route("/api/random_destinations/<int:flights>")
def random_destinations(flights):
    kohteet = GameState.random_destination(conn, flights)
    return jsonify([
        {"icao": icao, "name": nimi, "country": maa, "lat": lat, "lon": lon}
        for icao, nimi, maa, lat, lon in kohteet
    ])

if __name__ == "__main__":
    app.run(port=5000, debug=True)

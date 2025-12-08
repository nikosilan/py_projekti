from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

from aircraft_utils import GameState
from log_in import kirjautuminen

yhteys = kirjautuminen()

BASE_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "Daniel",
    "password": "DA10",
    "database": "flight_game",
    "autocommit": True
}

@app.route('/api/save-prize', methods=['POST'])
def save_prize():
    data = request.get_json()
    prize = data.get("prize", 0)

    try:
        GameState.raha_muutos(yhteys, prize)

        return jsonify({"message": f"Prize {prize}€ saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

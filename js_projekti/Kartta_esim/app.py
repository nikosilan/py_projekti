from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Palvelin etusivu
@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

# Palvelin CSS
@app.route("/style.css")
def css():
    return send_from_directory(os.getcwd(), "style.css")

# Palvelin JS
@app.route("/app.js")
def js():
    return send_from_directory(os.getcwd(), "app.js")

# API palauttaa simuloidun säädatan
@app.route("/api/saa", methods=["POST"])
def saa():
    data = request.get_json()
    lat = data.get("lat")
    lon = data.get("lon")

    simuloitu = {
        "lat": lat,
        "lon": lon,
        "saa": "Aurinkoista",
        "lampotila": 15 + int(lat) % 10
    }
    return jsonify(simuloitu)

if __name__ == "__main__":
    app.run(debug=True)

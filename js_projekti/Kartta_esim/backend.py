from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'flight_game',
    'user': 'niko',
    'password': 'salasana',
    'autocommit': True
}

@app.route("/api/airports")
def get_airports():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT name, ident AS icao, iso_country AS country,
               latitude_deg AS lat, longitude_deg AS lon
        FROM airport
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

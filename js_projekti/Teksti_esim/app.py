from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    # Palauttaa frontin index.html
    return send_from_directory(".", "index.html")

@app.route("/api/tervehdys")
def tervehdys():
    return "Hei! Tämä on backendin vastaus."

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, flash, redirect
from flask_game.aircraft_utils import GameState

app = Flask(__name__)
app.secret_key = "secret123"   # tai mikä tahansa muu merkkijono

@app.route("/")
def index():
    flash("Enter your name")
    return render_template("character_name.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form['name_input'] # tämän voi syöttää tietokantafunktioon
    if not name or len(name) < 1 or len(name) > 20 or " " in name:
        flash("Invalid name. Try again.")
        return redirect("/")

    # tässä välissä tietokantafunktiokutsu
    GameState.nimea_hahmo() #tähän argumenteiksi: yhteys, name, id=1

    flash("Hello " + str(request.form['name_input']) + "! Your name has now been saved.")
    return render_template("character_name.html")

if __name__ == "__main__":
    app.run(port=5002, debug=True)
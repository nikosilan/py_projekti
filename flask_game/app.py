from flask import Flask, jsonify, request, render_template
from log_in import kirjautuminen
from aircraft_game_flask import FlightGame, session
from aircraft_utils import GameSession

yhteys = kirjautuminen()
app = Flask(__name__)
game = FlightGame(yhteys)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_input", methods=["POST"])
def send_input():
    value = request.json.get("value")
    session.store_input(value)
    return jsonify({"status": "ok"})

@app.route("/get_output")
def get_output():
    user_input = session.get_input()

    # START GAME IF FIRST TIME
    if user_input is None and not session.output_buffer:
        text, choices = game.step("START")
        for line in text:
            session.write(line)
        session.set_choices(choices)

    elif user_input is not None:
        text, choices = game.step(user_input)
        for line in text:
            session.write(line)
        session.set_choices(choices)

    return jsonify({
        "text": session.get_output(),
        "choices": session.get_choices()
    })

@app.route("/reset_game", methods=["POST"])
def reset_game():
    global game, session
    session = GameSession()           # reset input/output buffers
    game = FlightGame(yhteys)         # reset flight game state
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=5001, debug=True)
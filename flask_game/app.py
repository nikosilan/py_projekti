from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from log_in import kirjautuminen
from aircraft_game_flask import FlightGame, session
from aircraft_utils import GameSession, GameState, Airport
from geopy.distance import geodesic
import random
from quiz import quiz as full_quiz
from flask import session as flask_session

TOTAL_QUESTIONS = 3

yhteys = kirjautuminen()
app = Flask(__name__, static_folder='static')
app.secret_key = "secretkey"
game = FlightGame(yhteys)
CORS(app)


# Pääpelin asiat
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/current_destinations")
def current_destinations():
    if not game.temp_data.get("destinations"):
        return jsonify([])

    dests = []
    for icao, name, country, lat, lon in game.temp_data["destinations"]:
        dests.append({
            "icao": icao,
            "name": name,
            "country": country,
            "lat": lat,
            "lon": lon
        })
    return jsonify(dests)


@app.route("/send_input", methods=["POST"])
def send_input():
    value = request.json.get("value")
    session.store_input(value)
    return jsonify({"status": "ok"})


@app.route("/get_output")
def get_output():
    user_input = session.get_input()
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
    session = GameSession()  # reset input/output buffers
    game = FlightGame(yhteys)  # reset flight game state
    return jsonify({"status": "ok"})


# Noppa pelin asiat
@app.route("/noppa")
def noppa():
    return render_template("noppa.html")


@app.route('/api/save-prize', methods=['POST'])
def save_prize():
    data = request.get_json()
    prize = data.get("prize")

    try:
        GameState.raha_muutos(yhteys, prize)

        return jsonify({"message": f"Prize {prize}€ saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Hahmon luonti asiat
@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name_input', '').strip()

    # Validation
    if not name or len(name) < 1 or len(name) > 20 or ' ' in name:
        return jsonify({"success": False, "message": "Invalid name. Try again."})

    GameState.nimea_hahmo(yhteys, name)

    return jsonify({"success": True, "message": f"Hello {name}! Your name has been saved."})


# Hae nykyinen sijainti
@app.route("/api/current_location")
def current_location():
    conn = yhteys

    result = Airport.get_current_airport(conn)

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


# Päivitä sijainti ja laske etäisyys (EMME SITÄ KÄYTTÄÄ, KOSKA PÄÄPELI JO TEKEE SITÄ)
'''@app.route("/api/set_destination", methods=["POST"])
def set_destination():
    data = request.get_json()
    new_icao = data.get("icao")

    if not new_icao:
        return jsonify({"success": False, "message": "ICAO puuttuu"}), 400

    conn = yhteys

    # Hae nykyinen sijainti
    current = Airport.get_current_airport(conn)
    # Hae valittu kohde
    new_airport = Airport.get_airport_info(new_icao, conn)

    if not current or not new_airport:
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
    })'''


# Tietokilpailu (Trivia Quiz) asiat
@app.route('/tietokilpailu')
def tietokilpailu():
    return render_template('trivia_quiz.html')

@app.route('/start_game')
def start_game():
    # Pick 3 random questions for this session
    flask_session['questions'] = random.sample(list(full_quiz.keys()), TOTAL_QUESTIONS)
    flask_session['current_index'] = 0
    flask_session['prize'] = 0
    return jsonify({"started": True})


@app.route('/get_question')
def get_question():
    idx = flask_session.get('current_index', 0)
    questions = flask_session.get('questions', [])

    if idx >= len(questions):
        total_prize = flask_session.get('prize', 0)
        flask_session.clear()
        return jsonify({"finished": True, "total_prize": total_prize})

    question = questions[idx]
    data = full_quiz[question]
    return jsonify({
        "question": question,
        "choices": data['choices']
    })


@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    question = data['question']
    user_answer = data['answer']

    correct_answer = full_quiz[question]['correct']
    reward = 0
    message = ""

    if user_answer == correct_answer:
        reward = random.randint(10, 200)
        flask_session['prize'] += reward
        message = f"Correct! You earned {reward}€!"
    else:
        message = "Wrong! You earned nothing."

    flask_session['current_index'] += 1
    finished = flask_session['current_index'] >= TOTAL_QUESTIONS
    total_prize = flask_session.get('prize', 0)

    if finished:
        flask_session.clear()

    return jsonify({
        "user": user_answer,
        "correct": correct_answer,
        "message": message,  # <- include message
        "finished": finished,
        "total_prize": total_prize
    })

@app.route('/api/save-prize-tietokilpailu', methods=['POST'])
def save_prize_tietokilpailu():
    data = request.get_json()
    prize = data.get('total_prize')

    try:
        GameState.raha_muutos(yhteys, prize)

        return jsonify({"message": f"Prize {prize}€ saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5001, debug=True)

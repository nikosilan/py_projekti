from flask import Flask, request, jsonify, session, send_from_directory, render_template
from flask_cors import CORS
from Trivia_Quiz.quiz import quiz as full_quiz
from aircraft_utils import GameState
from log_in import kirjautuminen
import random

yhteys = kirjautuminen()

app = Flask(__name__, static_folder="static_test")
app.secret_key = "secretkey"
CORS(app)

TOTAL_QUESTIONS = 3

@app.route('/')
def tietokilpailu():
    return render_template('trivia_quiz.html')

@app.route('/start_game')
def start_game():
    # Pick 3 random questions for this session
    session['questions'] = random.sample(list(full_quiz.keys()), TOTAL_QUESTIONS)
    session['current_index'] = 0
    session['prize'] = 0
    return jsonify({"started": True})


@app.route('/get_question')
def get_question():
    idx = session.get('current_index', 0)
    questions = session.get('questions', [])

    if idx >= len(questions):
        total_prize = session.get('prize', 0)
        session.clear()
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
        session['prize'] += reward
        message = f"Correct! You earned {reward}€!"
    else:
        message = "Wrong! You earned nothing."

    session['current_index'] += 1
    finished = session['current_index'] >= TOTAL_QUESTIONS
    total_prize = session.get('prize', 0)

    if finished:
        session.clear()

    return jsonify({
        "user": user_answer,
        "correct": correct_answer,
        "message": message,  # <- include message
        "finished": finished,
        "total_prize": total_prize
    })


if __name__ == "__main__":
    app.run(port=5100, debug=True)

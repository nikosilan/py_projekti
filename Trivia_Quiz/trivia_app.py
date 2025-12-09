from flask import Flask, request, render_template, flash, jsonify
from Trivia_Quiz.quiz import quiz
import random

app = Flask(__name__, static_folder="static_test")
app.secret_key = "salainenAvain"


@app.route('/')
def trivia_quiz():
    # Valitaan kysymys sanakirjasta
    question = random.choice(list(quiz.keys()))
    data = quiz[question]

    # Lähetetään kysymys ja vaihtoehdot HTML:lle
    return render_template("trivia_quiz.html",
                           question=question,
                           choices=data["choices"])


@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()

    question = data["question"]
    user_answer = data["answer"]
    correct_answer = quiz[question]["correct"]

    # Poistetaan kysytty kysymys sanakirjasta
    quiz.pop(question)

    return jsonify({
        "user": user_answer,
        "correct": correct_answer,
        "correct_is_user": (user_answer == correct_answer)
    })

if __name__ == "__main__":
    app.run(port=5100, debug=True)
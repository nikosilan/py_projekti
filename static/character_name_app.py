from flask import Flask, render_template, request, flash, redirect


app = Flask(__name__, template_folder='.')  

app.secret_key = "secret123"

@app.route("/")
def index():
    flash("Enter your name")
    return render_template("character_name.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get('name_input', '').strip()
    if not name or len(name) > 20 or " " in name:
        flash("Invalid name. Try again.")
        return redirect("/")

    flash(f"Hello {name}! Your name has now been saved.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

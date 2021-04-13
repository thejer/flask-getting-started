from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Message from the View form the 6.",
    )

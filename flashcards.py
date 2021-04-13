from flask import Flask, render_template

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Message from the View form the 6.",
    )


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)

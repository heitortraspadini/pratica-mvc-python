from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ciencia():
    return render_template("index.html", title = "Agenda")
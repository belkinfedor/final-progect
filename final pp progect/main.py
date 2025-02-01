from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def info():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

app.run(debug=True)


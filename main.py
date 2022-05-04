from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")

@app.route("/page1")
def go_to_page():
    return render_template("page1.html")
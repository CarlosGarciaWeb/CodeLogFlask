from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


# Here it will have a dynamic url passing the slug of the thread title
@app.route("/thread")
def thread():
    return render_template("thread.html")

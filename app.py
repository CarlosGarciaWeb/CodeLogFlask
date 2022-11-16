from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

entries_list = []

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        log_content = request.form.get("log")
        log_information = (log_content, datetime.now().strftime("%m/%d/%y"), datetime.now().strptime(datetime.now().strftime("%m/%d/%y"), "%m/%d/%y"))
        entries_list.append(log_information)
    kwargs = {
        "log_info": entries_list,
    }
    return render_template("index.html", **kwargs)


# Here it will have a dynamic url passing the slug of the thread title
@app.route("/thread")
def thread():
    return render_template("thread.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000)
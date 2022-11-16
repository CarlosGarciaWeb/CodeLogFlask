from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os





def create_app():
    app = Flask(__name__)

    mongo_pass_env = os.environ.get('MONGODB_PASS')

    client = MongoClient(f"mongodb+srv://carloswebdev:{mongo_pass_env}@micrologflask.1owutpp.mongodb.net/test")
    app.db = client.microlog

    @app.route("/", methods=["GET", "POST"])
    def home_page():
        if request.method == "POST":
            log_content = request.form.get("log")
            # log_information = (log_content, datetime.now().strftime("%m/%d/%y"), datetime.now().strptime(datetime.now().strftime("%m/%d/%y"), "%m/%d/%y"))
            app.db.logs.insert_one({"log_entry": log_content, "log_date": datetime.now().strftime("%m/%d/%y %H:%M")})
        kwargs = {
            "log_info": [entry for entry in app.db.logs.find({})],
        }
        return render_template("index.html", **kwargs)


    # Here it will have a dynamic url passing the slug of the thread title
    
    @app.route("/thread")
    def thread():
        return render_template("thread.html")


    return app



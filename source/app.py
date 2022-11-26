from flask import Flask, render_template, request
import os

app = Flask(__name__)
flag = open("flag.txt").read()
db = [i.strip() for i in open("database.db", "r").readlines()]
db.append(flag)
TEAM_LINK = os.getenv("TEAM_LINK")


def check_if_in(input):
    for record in db:
        if input in record:
            return True
    return False


@app.route("/")
def index():
    return render_template("index.html", TEAM_LINK=TEAM_LINK)


@app.route("/submit", methods=["POST"])
def check():
    req = request.data.decode("utf-8")
    return {"error": not check_if_in(req)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

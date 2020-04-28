from flask import Flask, render_template, request,redirect
from scrapper import get_jobs
app = Flask("CodingmeeeScrapper")

db = {}

@app.route("/")
def home():
    return render_template("codingmeee.html")
@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs))
@app.route("/<username>")
def potato(username):
    return f"Hello your name is {username}"
app.run(host="127.0.0.1")


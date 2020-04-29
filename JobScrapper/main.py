from flask import Flask, render_template, request,redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file
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
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                        jobs=jobs)
@app.route("/<username>")
def potato(username):
    return f"Hello your name is {username}"


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv",mimetype='text/csv',attachment_filename=f"{word}.csv",as_attachment=True)
    except:
        return redirect("/")


app.run(host="127.0.0.1")


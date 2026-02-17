from flask import Flask, request, render_template

app = Flask("__main__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

app.run()
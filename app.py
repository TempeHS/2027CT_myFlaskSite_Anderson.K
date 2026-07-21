from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/myprojects")
def myprojects():
    return render_template("myprojects.html")


@app.route("/rpmcounter")
def rpmcounter():
    return render_template("rpmcounter.html")


@app.route("/spinningtop")
def spinningtop():
    return render_template("spinningtop.html")


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

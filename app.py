from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return "about page"


@app.route("/contact")
def contact():  # Fixed typo from 'cotact'
    return "contact page"


if __name__ == "__main__":
    app.run(debug=True)
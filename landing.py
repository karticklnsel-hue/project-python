from flask import Flask

app = Flask(__name__)


@app.route("/landing")
def hello():
  return "Landing Page"


if __name__ == "__main__":
  app.run(debug=True)

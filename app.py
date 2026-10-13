from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return 'Hello, World! Go to LNSEL<br><br><a href="/about">About Us</a>&nbsp;<a href="/contact">Contact Us</a>'
  
@app.route("/about")
def about():
  return "about page"
  
@app.route("/contact")
def cotact():
  return "contact page"

if __name__ == "__main__":
  app.run(debug=True)

import os
from urllib.parse import quote_plus

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# ============================================================
# CHANGE ONLY THESE VALUES (copy from Railway > MySQL > Variables)
# ============================================================
DB_USER = "root"                      # MYSQLUSER
DB_PASSWORD = "your-password-here"    # MYSQLPASSWORD
DB_HOST = "your-host-here"            # public host, e.g. xxxx.proxy.rlwy.net
DB_PORT = "3306"                      # public port from Railway (NOT always 3306)
DB_NAME = "railway"                   # MYSQLDATABASE
# ============================================================

# On Render you can instead set an environment variable DATABASE_URL
# and it will be used automatically (no need to edit the values above).
DEFAULT_URI = (
    f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", DEFAULT_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True, "pool_recycle": 280}

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Create tables if they don't exist (won't crash the app if DB is unreachable)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("Database connection error:", e)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return "about page"


@app.route("/contact")
def contact():
    return "contact page"


# Test the database connection: open /dbtest
@app.route("/dbtest")
def dbtest():
    try:
        db.session.execute(db.text("SELECT 1"))
        return "Database connected successfully!"
    except Exception as e:
        return f"Database error: {e}", 500


# Add a user: open /add/John
@app.route("/add/<name>")
def add_user(name):
    db.session.add(User(name=name))
    db.session.commit()
    return f"Added {name}"


# List users: open /users
@app.route("/users")
def users():
    return {"users": [u.name for u in User.query.all()]}


if __name__ == "__main__":
    app.run(debug=True)

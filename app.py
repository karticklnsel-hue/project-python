import os
from urllib.parse import quote_plus

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# ============================================================
# CHANGE ONLY THESE VALUES (copy from Railway > MySQL > Variables)
# ============================================================
DB_USER = "demodevsol_python"      # database USER you create in Webuzo
DB_PASSWORD = "&njOsQ7!x!"    # that user's password
DB_HOST = "23.226.124.182"   # your server domain or server IP (not localhost)
DB_PORT = "3306"
DB_NAME = "demodevsol_python"         # database name from phpMyAdmin
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
    # Matches the existing "users" table in your Railway MySQL
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)


# Create tables if they don't exist (won't crash the app if DB is unreachable)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("Database connection error:", e)


@app.route("/")
def hello():
    try:
        all_users = User.query.order_by(User.id).all()
        error = None
    except Exception as e:
        all_users = []
        error = str(e)
    return render_template("index.html", users=all_users, error=error)


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


# JSON list of users (password is intentionally NOT included)
@app.route("/users")
def users():
    return {
        "users": [
            {"id": u.id, "user_name": u.user_name, "created_at": str(u.created_at)}
            for u in User.query.order_by(User.id).all()
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)

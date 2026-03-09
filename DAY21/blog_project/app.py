from flask import Flask
from flask_login import LoginManager
from models import db, User


app = Flask(__name__)

# ----------------------------
# Basic Configuration
# ----------------------------
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ----------------------------
# Initialize Database
# ----------------------------
db.init_app(app)

# ----------------------------
# Initialize Login Manager
# ----------------------------
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ----------------------------
# Create Database Tables
# ----------------------------
with app.app_context():
    db.create_all()

# ----------------------------
# Basic Test Route
# ----------------------------
@app.route("/")
def home():
    return "Blog App Running 🚀"

from routes import main
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True, port = 8000)
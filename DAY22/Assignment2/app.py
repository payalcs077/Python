from flask import Flask, render_template, redirect, url_for
from models import db, User
from forms import UserForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("users"))

    return render_template("index.html", form=form)

@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template("user.html", users=all_users)

if __name__ == "__main__":
    app.run(debug=True)
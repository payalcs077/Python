import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime


app = Flask(__name__)

# load_dotenv()

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit

db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content")
        file = request.files.get("image")

        filename = None

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_task = Todo(content=content, image=filename)

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("index"))

    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)

    if task.image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], task.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/complete/<int:id>")
def complete(id):
    task = Todo.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

#user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(200), nullable = False) # admin / author / user
    posts = db.relationship(
    'Post',
    backref='author',
    lazy=True,
    cascade="all, delete-orphan"
)

#post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(200), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  
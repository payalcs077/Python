from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(1000),nullable = False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
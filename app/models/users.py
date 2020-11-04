from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text) 
    password = db.Column(db.Text) 
    posts = db.relationship('Post', backref='author', lazy=True)
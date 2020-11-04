from . import db
from flask_login import UserMixin
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255)) 
    password = db.Column(db.String(255))

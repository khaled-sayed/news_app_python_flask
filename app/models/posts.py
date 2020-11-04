from . import db
import datetime

class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    img = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cate_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    trending = db.Column(db.Integer, nullable=True)

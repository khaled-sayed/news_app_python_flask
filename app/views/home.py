from flask import Blueprint, render_template, jsonify, request
from app.models.posts import Post
from sqlalchemy import func,desc
import datetime


home = Blueprint('home',__name__)

@home.route('/')
def home_page():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by().limit(5).all()
    posts_Trend = Post.query.order_by(desc(Post.trending)).limit(5).all()
    posts_news = Post.query.filter_by(cate_id=2).limit(5).all()
    all_news = Post.query.order_by(Post.created.desc()).paginate(page=page ,per_page=5)
    last_news = Post.query.order_by(desc(Post.created)).limit(9).all()
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")
    day_name  = now.strftime("%a")
    time = now.strftime("%X")
    all_day  = day_name + ' ' + day + ' ' + month + ' ' + year + ' ' +time
    # time = posts.created.strftime("%c")
    return render_template('home/index.html',all_news=all_news, posts=posts, date=all_day, posts_trending=posts_Trend, posts_news=posts_news,last_news=last_news)

@home.route('/single/<int:id>')
def single_page(id):
    post = Post.query.filter_by(id=id).first()
    last_news = Post.query.order_by(desc(Post.created)).limit(9).all()
    posts_Trend = Post.query.order_by(desc(Post.trending)).limit(5).all()
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")
    day_name  = now.strftime("%a")
    time = now.strftime("%X")
    all_day  = day_name + ' ' + day + ' ' + month + ' ' + year + ' ' +time
    return render_template('home/single.html',post=post, last_news=last_news,posts_trending=posts_Trend, date=all_day)
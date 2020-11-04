from flask import Blueprint, render_template, request, redirect, flash, url_for, make_response
from app.models.categories import Categorie,db
from app.models.posts import Post
from app.models.users import User
from app.forms.add_category import AddCategoryForm
from app.forms.add_artical import AddArticalForm
from flask_login import login_required
import os
from sqlalchemy import desc,asc
from werkzeug.utils import secure_filename
from app import test
dash = Blueprint('dash',__name__)

@dash.route('/dashboard')
@login_required
def dash_home():
    pageTitle = 'الرئيسية' 
    return render_template('dashboard-home/dashboard.html', pageTitle= pageTitle)

@dash.route('/add-category', methods=['GET','POST'])
@login_required
def add_category():
    pageTitle = 'إضافة قائمة'
    form = AddCategoryForm()
    if request.method == 'GET':
        return render_template('dashboard-home/add_category.html', form=form, pageTitle=pageTitle)
    
    name_category = request.form.get('name')
    category = Categorie.query.filter_by(name=name_category).first()
    if category:
        flash('يوجد هذه القائمة من قبل')
        return redirect(url_for('dash.add_category'))

    if form.validate_on_submit():
        category = Categorie(name=name_category)
        db.session.add(category)
        db.session.commit()
        flash('تم إضافة القائمة بنجاح')
        return redirect(url_for('dash.add_category'))
    
@dash.route('/add-artical', methods=['GET','POST'])
@login_required
def add_artical():
    pageTitle = 'إضافة مقال'
    form_artical = AddArticalForm()
    form_artical.category.choices = [(cate.id,cate.name)for cate in Categorie.query.all()]
    if request.method == 'GET':
        return render_template('dashboard-home/add_artical.html', form=form_artical,pageTitle=pageTitle)

    title = request.form.get('title')
    body = request.form.get('body')
    author = request.form.get('author')
    img = request.files.get('img')
    category = request.form.get('category')
    if img:
        path = os.path.join(test, img.filename)
        img.save(path)
    if form_artical.validate_on_submit():
        author = User.query.filter_by(username='khaled').first()
        cate = Categorie.query.filter_by(id=category).first()
        post = Post(title=title, body=body, user_id=author.id, img=img.filename, cate_id=cate.id)
        db.session.add(post)
        db.session.commit()
        flash('تم إضافة المقال بنجاح')
        return redirect(url_for('dash.add_artical'))

@dash.route("/all-articals")
@login_required
def all_articals():
    pageTitle = 'المقالات'
    posts = Post.query.order_by(desc(Post.id)).all()
    author = User.query.all()
    category = Categorie.query.all() 
    return render_template('dashboard-home/articals.html', pageTitle=pageTitle, posts=posts, author=author, categories=category)

@dash.route("/delete-artical/<int:id>", methods=["GET"])
@login_required
def delete_artical(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    flash('تم حذف المقال بنجاح')
    return redirect(url_for('dash.all_articals'))

@dash.route("/edit-artical/<int:id>", methods=["GET","POST"])
@login_required
def edit_artical(id):
    pageTitle = 'تعديل المقال'
    form_artical = AddArticalForm()
    if request.method == 'GET':
        post = Post.query.filter_by(id=id).first()
        form_artical.body.data = post.body
        form_artical.category.choices = [(cate.id,cate.name)for cate in Categorie.query.all()]
        return render_template('dashboard-home/edit_artical.html', form=form_artical,pageTitle=pageTitle, post=post)

    post_id = request.form.get('id')
    category = request.form.get('category')
    post = Post.query.filter_by(id=post_id).first()
    cate = Categorie.query.filter_by(id=category).first()
    img = request.files.get('img')
    author = request.form.get('username')

    post.title = request.form.get('title')
    post.body = request.form.get('body')
    post.cate_id = cate.id
    if img and img.filename != post.img:
        path = os.path.join(test, img.filename)
        img.save(path)
        post.img = img.filename
    db.session.commit()
    flash('تم تعديل المقال بنجاح')
    return redirect(url_for('dash.all_articals'))
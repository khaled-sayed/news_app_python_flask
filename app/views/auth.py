from flask import Blueprint, request,render_template, flash, redirect, url_for, session
from app import db, app
from app.models.admins import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)


@auth.route('/admin/login', methods=['POST','GET'])
def admin_login():
    if request.method == 'GET':
        return  render_template('auth/admin-login-page.html')

    email = request.form.get('email')
    password = request.form.get('password')

    admin = Admin.query.filter_by(email=email).first()
    if not admin or not check_password_hash(admin.password, password):
        flash('Please Check your login details and try agin .')
        return redirect(url_for('auth.admin_login'))
    
    login_user(admin)
    session['username'] = current_user.username
    return redirect(url_for('dash.dash_home'))

@auth.route('/admin/logout')
@login_required
def logout():
    session.pop('username', None)
    logout_user()
    return 'Loged out'
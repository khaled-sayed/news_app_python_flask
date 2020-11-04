from flask import Flask, render_template
from dotenv import load_dotenv
import config
import os
from flask_login import LoginManager
from werkzeug.utils import secure_filename
base = os.path.dirname(os.path.abspath(__name__))
UPLOAD_FOLDER = 'app/static/images/upload/news'
# ALLOWED_EXTINSTIONS = set(['jpeg','jpg','png'])

app = Flask(__name__)
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dontenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dontenv_path)
app.config.from_object('config.settings.'+ os.environ.get('FLASK_ENV'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
test = app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app.models import db
from app.models.admins import Admin
from app.models.categories import Categorie
from app.models.posts import Post
from app.models.users import User

db.create_all()
db.session.commit()
login_manger = LoginManager()
login_manger.login_view = 'auth.admin_login'
login_manger.init_app(app)


# Create Page Not Found
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@login_manger.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# Register BluePrints 
from app.views.auth import auth as auth_blueprint
from app.views.dashboard import dash as dash_blueprint
from app.views.home import home as home_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(dash_blueprint)
app.register_blueprint(home_blueprint)
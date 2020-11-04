import os
base = os.path.dirname(os.path.abspath(__name__))
class Config:
    """ basic configrations. """
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(base, 'news.db')
    # "mysql+pymysql://root:@localhost/news"
    # 'sqlite:///' + os.path.join(base, 'app.db')
    #"mysql+pymysql://root:@localhost/twitter"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "khaled@12345"
    JWT_SECRET_KEY = "64356351as5d6a5s"
    JWT_TOKEN_LOCATION = ['cookies']

class development(Config):
    DEBUG = True

class productino(Config):

    PORT = os.environ.get('PORT') or 8080
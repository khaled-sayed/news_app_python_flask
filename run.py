# run application object from our app package
from app import app

if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])

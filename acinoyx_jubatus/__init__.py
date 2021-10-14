from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1ab2c3d4e5f6g7'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, ur_lprefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
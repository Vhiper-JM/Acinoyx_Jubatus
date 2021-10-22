import sqlite3 as sql
from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1ab2c3d4e5f6g7'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, ur_lprefix='/')
    app.register_blueprint(auth, url_prefix='/')


    #conn = sql.connect('database.db')
    #print("exitoso")
    #conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, profile_photo BLOB, email TEXT, user_name TEXT, password TEXT, age INT )')
    #conn.execute('CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, photo BLOB, foot_note TEXT, post_date TEXT, user_id INT, FOREIGN KEY(user_id) REFERENCES users(id))')
    #conn.execute('CREATE TABLE comments (id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INT, comment TEXT, user_id INT, date TEXT, like INT, FOREIGN KEY(user_id) REFERENCES users(id) , FOREIGN KEY(post_id) REFERENCES posts(id))')
    #conn.close()


    return app
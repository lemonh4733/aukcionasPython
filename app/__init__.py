from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

App = Flask(__name__)
App.config['SECRET_KEY'] = "becf55ac435bb4faa6c925ec354b84b5"
App.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(App)
login_manager = LoginManager(App)
login_manager.login_view = "login"
login_manager.login_message_category = "danger"

import app.controllers.home
import app.controllers.auth
import app.controllers.item
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpengo.db'
#app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'
#db = SQLAlchemy(app)

#blueprint for auth routes
#from .auth import auth as auth_blueprint

#from core import routes
#import core.alpengo_data as alpengo_data


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/alpengo.db"
app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from core import routes
import core.alpengo_data as alpengo_data

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpengo.db'
app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'
db = SQLAlchemy(app)

from core import routes
import core.alpengo_data as alpengo_data
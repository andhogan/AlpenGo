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
from flask_login import LoginManager 

# init SQLAlchemy so we can use it in our models
db = SQLAlchemy()


app = Flask(__name__)

app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpengo.db'
    
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.userID

# blueprint for auth routes in our app
from core.auth_routes import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from core.routes import routes as main_blueprint
app.register_blueprint(main_blueprint)

@app.before_first_request
def create_tables():
    db.create_all()
from flask import Flask
from core import app

import unittest

from core import db
from core.models import user_achievement, user_peak, User, Peak, Achievement

class dbTest(unittest.TestCase):

    def setUp(self):
        ####################################
        ###Create a new Db for unit tests###
        ####################################
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        ##################################
        ###Remove all items from the Db###
        ##################################

        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

    def createUser(self):
        user1 = User(firstName="Alex", lastName="Jocius", userName="aljo", emailAddress="aljo@colorado.edu", password="password")
        db.session.add(user1)
        db.session.commit()
        ret = User.query.all()
        print(ret)
        self.assertEqual(user1.firstName == "Alex")
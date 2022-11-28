from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core import app, db
from core.models import *


def addPeak():
    new_peak = Peak(name='Mt Elbert', startElevation=9700, summitElevation=14438, elevationGain=5300,
                    length=11.00, avTime=8.00, routeType='Out and Back', peakClass=2,
                    description='The highest summit in Colorado, Mt Elbert offers stunning views of \
                    the surrounding Rocky Mountains.')

    db.session.add(new_peak)
    db.session.commit()

    print("done")

    return True
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core import db
from core.models import *

#####################################################################################
######################Data for Peak List offered in AlpenGo##########################
#####################################################################################

Peaks = [{
    'PeakID': 1,
    'Name': 'Mt Elbert',
    'StartElev': 9700,
    'SummitElev': 14438,
    'ElevGain': 5300,
    'Length': 11.00,
    'Avtime': 8.00,
    'RouteType': 'Out and Back',
    'Class': 2,
    'Description': 'The highest summit in Colorado, Mt Elbert offers stunning views of the surrounding Rocky Mountains.'},
    {'PeakID': 2,
    'Name': 'Mt Evans',
    'StartElev': 12850,
    'SummitElev': 14268,
    'ElevGain': 1650,
    'Length': 5.25,
    'Avtime': 3.75,
    'RouteType': 'Out and Back',
    'Class': 3,
    'Description': 'Generally conisdered a challenging route, Mt Evans is one of six front range 14ers.  Keep an eye out for bighorn sheep and summer wildflowers.'},
    {'PeakID': 3,
    'Name': 'Capitol Peak',
    'StartElev': 9450,
    'SummitElev': 14138,
    'ElevGain': 5300,
    'Length': 17.00,
    'Avtime': 9.75,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'Often called the most difficult 14er in Colorado, its rugged terrain and extreme slopes will prove to be a challenge for even the most experienced hikers.'},
    {'PeakID': 4,
    'Name': 'North Maroon Peak',
    'StartElev': 9590,
    'SummitElev': 14022,
    'ElevGain': 4500,
    'Length': 9.25,
    'Avtime': 7.00,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'One of the most iconic 14ers in Colorado, this picturesque mountain is a technical challenge, challenging hikers with its rugged terrain and route-finding.'},
    {'PeakID': 5,
    'Name': 'Quandary Peak',
    'StartElev': 10850,
    'SummitElev': 14272,
    'ElevGain': 3450,
    'Length': 6.75,
    'Avtime': 5.25,
    'RouteType': 'Out and Back',
    'Class': 1,
    'Description': 'A beginner friendly summit, Quandary Peak is less than a two hour drive from Denver and offers panoramic views of the surrounding terrain.'},
    {'PeakID': 6,
    'Name': 'Crestone Needle',
    'StartElev': 9900,
    'SummitElev': 14196,
    'ElevGain': 4400,
    'Length': 11.25,
    'Avtime': 10.00,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'One of the more challengine 14er peaks in Colorado, Crestone Needle has high exposure and requires strong route finding skills. Attempt this peak with extreme caution.'},
    {'PeakID': 7,
    'Name': 'Huron Peak',
    'StartElev': 10560,
    'SummitElev': 14006,
    'ElevGain': 3500,
    'Length': 6.50,
    'Avtime': 3.00,
    'RouteType': 'Out and Back',
    'Class': 2,
    'Description': 'This beginner friendly summit offers the same challenge as Mount Bierstadt but without the crowds. Although non-technical, be ready for a long and steady hike.'},
    {'PeakID': 8,
    'Name': 'Longs Peak',
    'StartElev': 9400,
    'SummitElev': 14259,
    'ElevGain': 5100,
    'Length': 14.50,
    'Avtime': 12.00,
    'RouteType': 'Out and Back',
    'Class': 3,
    'Description': 'This peak in the Rocky Mountain National Park deserves respect for the trek that can take between 10 to 15 hours. The views of Clavier George, Black Lake, and Powell Peak are worth the effort.'},
    {'PeakID': 9,
    'Name': 'Grays Peak',
    'StartElev': 11280,
    'SummitElev': 14275,
    'ElevGain': 3000,
    'Length': 7.50,
    'Avtime': 5.25,
    'RouteType': 'Out and Back',
    'Class': 1,
    'Description': 'One of the closest 14ers to Denver, this relatively easy summit does not require any technical knowledge. For an added experience, hike the nearby Torreys Peak.'},
    {'PeakID': 10,
    'Name': 'Little Bear Peak',
    'StartElev': 8000,
    'SummitElev': 14041,
    'ElevGain': 6200,
    'Length': 14.00,
    'Avtime': 11.50,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'This standard route requires some tough scrambling and high level of exposure, hikers should use extreme caution when hiking this infamous peak.'},
]

#####################################################################################
#####################################################################################


####################################################################################
#########################Helper functions for Db Operations#########################
####################################################################################


# Add all peaks from Peaks List to the Db if not currently stored in Db
def addPeaks():
    for peak in Peaks:
        peak_db = db.session.execute(db.select(Peak).filter_by(name=peak['Name'])).scalar()
        if not peak_db:
            new_peak = Peak(name=peak['Name'], startElevation=peak['StartElev'], summitElevation=peak['SummitElev'], elevationGain=peak['ElevGain'],
                            length=peak['Length'], avTime=peak['Avtime'], routeType=peak['RouteType'], peakClass=peak['Class'],
                            description=peak['Description'])

            db.session.add(new_peak)
            db.session.commit()

    print("done")

    return True

# Delete all peaks from the Peak table within the Db
def delPeaks():
    db.session.query(Peak).delete()
    db.commit()
    return True


#Add dummy data Users to db

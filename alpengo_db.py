"""Run this script with 'python alpengo_db.py' 
to construct a SQLite DB filled with our dummy data"""

import core.alpengo_data as alpengo_data
import sqlite3
import os

# if __name__ == '__main__':
#     dbname = './alpengo_db' #Initialize

dbname = './alpengo_db' #Initialize

conn = sqlite3.connect(dbname)
c = conn.cursor()

### Construct Tables ###

# Users

c.execute("""CREATE TABLE IF NOT EXISTS Users
(
UserID                      integer PRIMARY KEY,
FirstName                   varchar,
LastName                    varchar,
UserName                    varchar UNIQUE,
EmailAddress                varchar UNIQUE,
Password                    varchar,

TotalDistance               float DEFAULT 0,
MountainsHiked              tinyint DEFAULT 0,
TotalTime                   float DEFAULT 0,
NumAchievements             tinyint DEFAULT 0,
TotalElevGain               float DEFAULT 0
);
""") #Location omitted for now

# Peaks

c.execute("""CREATE TABLE IF NOT EXISTS Peaks
(
PeakID                 integer PRIMARY KEY,
Name                   varchar,

StartElevation         integer,
SummitElevation        integer,
ElevationGain          integer,
Length                 float,
AvTime                 float,
RouteType              varchar,
Class                  tinyint,
Description            varchar NULL
);
""") #Location omitted for now

# Achievements

c.execute("""CREATE TABLE IF NOT EXISTS Achievements
(
AchievementID                 integer PRIMARY KEY,
Achievement                   varchar,
Description                   varchar NULL
);
""")

# UserPeaks Relationship

c.execute("""CREATE TABLE IF NOT EXISTS UserPeaks
(
UserID                 integer NOT NULL,
PeakID                 integer NOT NULL,
Date                   Date,
StartTime              DateTime,
EndTime                DateTime,
Miles                  Float,
AverageHR              tinyint,
Steps                  integer,
  FOREIGN KEY (UserID) REFERENCES Users(UserId),
  FOREIGN KEY (PeakID) REFERENCES Peaks(PeakID)
);
""")

# UserAchievement Relationship

c.execute("""CREATE TABLE IF NOT EXISTS UserAchievement
(
UserID                 integer NOT NULL,
AchievementID          integer NOT NULL,
  FOREIGN KEY (UserID) REFERENCES Users(UserId),
  FOREIGN KEY (AchievementID) REFERENCES Achievements(AchievementID)
);
""")

### Fill Tables ###

# Users

insert_string_list= []
for user in alpengo_data.Users:
    insert_string = ""
    for key in user.keys():
        insert_string = insert_string+", "+"'"+str(user[key])+"'"
    #print(insert_string.lstrip(", "))
    insert_string_list.append(insert_string.lstrip(", "))
    
#print(insert_string_list)

for insert_string in insert_string_list:
    insert_cmd = f"INSERT INTO Users VALUES ({insert_string})"
    conn.execute(insert_cmd)

# Achievements

insert_string_list= []
for badge in alpengo_data.Achievements:
    insert_string = ""
    for key in badge.keys():
        insert_string = insert_string+", "+"'"+str(badge[key])+"'"
    #print(insert_string.lstrip(", "))
    insert_string_list.append(insert_string.lstrip(", "))
    
#print(insert_string_list)

for insert_string in insert_string_list:
    insert_cmd = f"INSERT INTO Achievements VALUES ({insert_string})"
    conn.execute(insert_cmd)

# Peaks

insert_string_list= []
for peak in alpengo_data.Peaks:
    insert_string = ""
    for key in peak.keys():
        insert_string = insert_string+", "+"'"+str(peak[key])+"'"
    #print(insert_string.lstrip(", "))
    insert_string_list.append(insert_string.lstrip(", "))
    
#print(insert_string_list)

for insert_string in insert_string_list:
    insert_cmd = f"INSERT INTO Peaks VALUES ({insert_string})"
    conn.execute(insert_cmd)

# UserPeaks

insert_string_list= []
for user_peak in alpengo_data.UserPeaks:
    insert_string = ""
    for key in user_peak.keys():
        insert_string = insert_string+", "+"'"+str(user_peak[key])+"'"
    #print(insert_string.lstrip(", "))
    insert_string_list.append(insert_string.lstrip(", "))
    
#print(insert_string_list)

for insert_string in insert_string_list:
    insert_cmd = f"INSERT INTO UserPeaks VALUES ({insert_string})"
    conn.execute(insert_cmd)

# UserAchievement

insert_string_list= []
for user_badge in alpengo_data.UserAchievement:
    insert_string = ""
    for key in user_badge.keys():
        insert_string = insert_string+", "+"'"+str(user_badge[key])+"'"
    #print(insert_string.lstrip(", "))
    insert_string_list.append(insert_string.lstrip(", "))
    
#print(insert_string_list)

for insert_string in insert_string_list:
    insert_cmd = f"INSERT INTO UserAchievement VALUES ({insert_string})"
    conn.execute(insert_cmd)

### Commit Changes, Close DB ###

conn.commit()
conn.close()
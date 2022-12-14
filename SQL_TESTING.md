# Database Visual
![Database Design](https://user-images.githubusercontent.com/104743365/199325220-3112257c-4322-4e7c-8f99-c092316cd203.JPG)

# Table and Test Descriptions

## Table 1

### Table Name
  Peaks
### Table Description
  Database object to store all information related to each specific mountain peak listed on the website.
### Table Fields
  * PeakID (*Int*) – Unique identifier to identify each peak.
  * Name (*VarChar*) – The name of the mountain peak.
  * Location (*Float*, *Float*) – Latitude and Longitude of the mountain peak.
  * StartElevation (*Int*) – The starting elevation of the peak trail in feet.
  * SummitElevation (*Int*) – The elevation at the mountain summit in feet.
  * ElevationGain (*Int*) – The total elevation gain during the hike.
  * Length (*Float*) – The total distance of the trail in miles.
  * AvTime (*Float*) – The average time to completion for all hikers in hours.
  * RouteType (*VarChar*) – A description of the type of trail for the peak.
  * Class (*Int*) – The difficulty of the hike.
  * Description (*VarChar*) – A description of the mountain peak and trail.
### List of Tests
  * *test_addPeak()* - addPeak() will take in values for each field listed above and return True if successful or False if an error occured.  This test function will run a number of assert statements to:
    * Check if all fields are inserted with their correct type and are not null
    * Check if values are in correct range
    * Check if all peaks were added by querying databse
    * Check to make sure a distinct count produces the correct number of peaks after they are added.
  * *test_deletePeak()* - deletePeak() will take in a peak name and delete the entry from the database. This test function will check to ensure the entry has been                               removed and the total count of entries has been reduced.
  * *test_modifyPeakAttr()* - modifyPeakAttr() will take in a peak name, a field name, and the corrected value, and will modify the entry.  This test fuction will run                               a number of assert statement on a number of entries to ensure it is working properly.

### Data Access Method 1

### Use case name
  Verify peak selection list.
### Description
  Test the rendering of the *Peak Selection* page.
### Pre-conditions
  User has an account and is logged in.
### Test Steps
  1. Login to user account.
  2. Navigate to the page menu on the home page.
  3. Click on *Peaks*.
### Expected Results
  The *Peak Selection* page should be rendered with a list of available peaks.
### Actual Results
  User is navigated to *Peak Selection* page and can scroll through list.
### Status (Pass/Fail)
  Pass
### Post-conditions
  User can select from the list of available peaks.  The page has successfully pulled from the database.

### Data Access Method 2

### Use case name
  Verify peak selection of the user.
### Description
  Test to ensure the user can select a specific peak to navigate to the *Peak* page.
### Pre-conditions
  User has an account and is logged in.
### Test Steps
  1. Login to user account.
  2. Navigate to the page menu on the home page.
  3. Click on *Peaks*.
  4. Click on a specific peak from the list.
### Expected Results
  User should see the *Peak* page with associated info displayed.
### Actual Results
  User sees the *Peak* page with mountain and user info displayed.
### Status (Pass/Fail)
  Pass
### Post-conditions
  Peak information is validated through database and is displayed on screen.
  
## Table 2

### Table Name
  UserPeaks
### Table Description
  Database object to store all information related to peaks each user has hiked and forming a many-to-many relationship.
### Table Fields
  * UserID (*Int*) – Unique identifier to identify each user.
  * PeakID (*Int*) – Unique identifier to identify each peak.
  * Date (*Date*) – The date the user hiked the distinct peak.
  * StartTime(*DateTime*) – The starting time that the user hiked the peak.
  * EndTime (*DateTime*) – The ending time that the user finished the hike.
  * Miles (*Float*) – The total miles hiked during the climb.
  * AvHr (*Int*) – The average heat rate experienced by the user during the hike.
  * Steps (*Int*) – The total steps taken during the hike.
### List of Tests
For all test, dummy data will be inserted into the database to create fake users and test data.
* *test_logHike()* - logHike() will take in a username, peak name, and all related fields above and record the entry in the UserPeaks table within the databse.  This test function will use assert statements to ensure:
  * All entries are not null and valid types for each field.
  * The user and peak exists within the database.
  * The data is stored in the database and can be queried.
  * The user cannot record the same hike twice.
* *test_getPeakRecord()* - getPeakRecord() will take in a username and peakname and will return null if no entry is found or return an array of data entries.  This test function will use a series of assert statements to ensure:
  * The user and peak exists in the database.
  * The data is returned properly.
### Data Access Method 1

### Use case name
  Verify the *Hike Log* button tracks user data.
### Description
  Test the *Hike Log* button by ensuring user input is stored within database.
### Pre-conditions
  User has an account, is logged in, and is on a specific peak page.
### Test Steps
  1. Login to user account.
  2. Navigate to the page menu on the home page.
  3. Click on *Peaks*.
  4. Click on a specific peak in the list.
  5. Click on Log Hike.
  6. Fill in data for each field.
  7. Click on Save Log.
### Expected Results
  The *Peak* page should be rendered with user data.
### Actual Results
  User is navigated back to *Peak* page and the user data is now displayed on screen.
### Status (Pass/Fail)
  Pass
### Post-conditions
  User can review his or her stats on the *Peak* page or navigate back to the *Peak Selection* page.
  
___

## Table 3

### Table Name
  Achievements
### Table Description
  Database object to store all information related achievements/badges users can acquire for attempting and/or completing hiking trails
### Table Fields
  * AchievementID (*Int*) - Unique identifier/Primary Key for uniquely identifying achievements
  * Achievement (*Varchar*) - Name of the achievement
  * Description (*Varchar*) - Description of the achievement/conditions for acquisition
### List of Tests
  * *test_addAchievement()* - addPeak() will take in values for each field listed above except ID and return True if successful or False if an error occured.  This test function will run a number of assert statements to:
    * Check that inserted values are unique, abiding my primary key

### Data Access Method 1

### Use case name
  Verify achievements render on users' profile pages
### Description
  Test the rendering of the *Achievement* page.
### Pre-conditions
  User has an account and is logged in.
### Test Steps
  1. Login to user account.
  2. Navigate to the Achievement page within the user profile (maybe home menu)
  3. Click on *Achievements*.
### Expected Results
  The *Achievement* page should be rendered with a list of available achievements along with their descriptions as to their acquisition.
### Actual Results
  User is navigated to *Achievement* page and can scroll through list.
### Status (Pass/Fail)
  Pass
### Post-conditions
  User can scroll the list of achievements, marveling at the ones they have acquired as well as challenging themselves to seek ones they haven't.  The page has successfully pulled from the database.
  
## Table 4

### Table Name
  UserAchievement
### Table Description
  Database object to store all information related to achievements each user has acquired and forming a many-to-many relationship. 
### Table Fields
  * UserID (*Int*) – Unique identifier to identify each user.
  * AchievementID (*Int*) - A record of the achievement the user has acquired
### List of Tests
For all test, dummy data will be inserted into the database to create fake users and test data.
* *test_awardAchievement()* - awardAchievement() will take in a username and an achievementID and add a record to the UserAchievement table.
  * Assert the user is not receiving a duplicate entry.
  * Assert the user has the qualifying conditions/stats for an achievement
* *test_getUserAchievement()* - getUserAchievement() will take in a username and return all acquired Achievements the user currently possesses.
  * The user exists in the Users table
  * The data is rendered to page properly
### Data Access Method 1

### Use case name
  Verify the *Achievements* page renders all acquired user achievements
### Description
  Test the *Achievement* page by ensuring appropriate achievements are listed at the top and colorized and unacquired achievements are below these and grayscaled. 
### Pre-conditions
  User has an account, is logged in, and isviewing the achievements page.
### Test Steps
  1. Login to user account.
  2. Navigate to the User Profile on the home page.
  3. Click on *User Profile*.
  4. Click on *Achievements*.
  5. View acquired achievements and read about ones yet to be acquired.
### Expected Results
  The *Achievements* page should be rendered with user data.
### Actual Results
  User is navigated to *Achievement* page and the user data is now displayed on screen.
### Status (Pass/Fail)
  Pass
### Post-conditions
  User can review his or her stats on the *Achievement* page and navigate away from this page.

## Table 5

### Table Name
  Users
### Table Description
  Database object to store all information related to the user. This will be a many to many relationship.
### Table Fields
  * UserID (*Int*) – Unique identifier automatically generated.
  * FirstName (*VarChar*) – User input of their first name.
  * LastName (*VarChar*) – User input of their last name.
  * UserName (*VarChar*) – Unique to the user, user input.
  * EmailAddress (*VarChar*) – Unique user inputted contact information.
  * Password (*VarChar*) – Unique user inputted statement that follows certain parameters.
  * Location (*Float,Float*) – Longitude and Latitude of the user’s location.
  * TotalDistance (*Float*) – Distance the user has personally hiked and logged correctly from the UserPeaks table.
  * MountainsHiked (*VarChar*) - List of all mountain names taken from the UserPeaks table using PeakID.
  * TotalTime (*Float*) - Total time it has taken the user to complete the total distance hiked. From the UserPeaks table.
  * NumAchievements (*Int*) - Quick overview of how many achievements the user has accumulated. Takes AchievementID from the UserAchievement table.
  * TotalElevGain (*Float*) - The total amount of elevation gained by the user along with the total distance and total time. Taken from the Peaks table.
### List of Tests
For all tests, dummy data will be inserted into the database to create fake users and test data.

* *test_createAccount()* - createAccount() will take in a username, first name, last name, password, email address, and location. The information will be recorded in the Users table within the database. This test function will use assert statements to ensure:
  * All entries are not null and valid types for each field.
  * The user exists within the database after creation.
  * The data is stored in the database and can be queried.
  * The user has used unique input for all required fields.
  * The password satisfies certain criteria.
  * The username has been generated properly.

* *test_logIn()* - logIn() will take the username and password entered on the log in screen and return the connected user's account. If the credentials do not match any in the database, an error will be returned. It will ensure that:
  * The username and password are stored in the database and that they match for one UserID.
  * The log in button works as intended.
  * The user's account is served to them correctly.

* *test_getPeakStats()* - getPeakStats() will take in a userID and populate the Users table with information from the UserPeaks table and the Peaks table, which will use the PeakID from the UserPeaks table to connect the information. This test will ensure that :
  * The data is returned properly.
  * The UserID and PeakIDs are valid.
* *test_getAchievementStats()* - getAchievementStats() will use the UserId to query the UserAchievement table and tally up the number of achievements the user has accumulated. It will be ensured that:
  * The data is returned properly.
  * The UserID is valid.
  * The AchievementID is valid.
### Data Access Method
### Use case name
  Verify the *Create Account* button takes in user input.
### Description
  Test the *Create Account* button by ensuring user input is stored within the database and is correct.
### Pre-conditions
  User has navigated to the webpage.
### Test Steps
  1. Type in the URL for the site.
  2. Navigate to the page menu on the home page.
  3. Click on *Log In*.
  4. Click on *Create Account*.
  5. Fill in all the required information.
  6. Click *Save*.
  7. Navigate back to the page menu and click *Profile*.
### Expected Results
  The *Profile* page should be rendered with user data.
### Actual Results
  User is navigated back to *Profile* page and the user data is now displayed on screen.
### Status (Pass/Fail)
  Pass
### Post-conditions
  User can review their stats on the *Profile* page or navigate back to the page menu and home page.

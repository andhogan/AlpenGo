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
  * *test_numPeaks()* – Query the database to ensure the total count of distinct peaks is equal to 10.
  * *test_peakNames()* – Pass in an array of peak names to ensure all peaks are stored in the database.
  * *test_location()* – Pass in three peak names to ensure that their correct locations are returned.
  * *test_elevation()* – Pass in three peak names to ensure that their starting, summit and elevation gains are returned correctly.
  * *test_length()* – Pass in three peak names to ensure their correct length is returned.
  * *test_avTime()* – Pass in three peak names to ensure their correct times are reported.
  * *test_routeType()* – Pass in three peak names to ensure their correct route type is returned.
  * *test_class()* – Pass in three peak names to ensure their correct classes are returned.
  * *test_description()* – Pass in three peak names to ensure their correct description is returned.

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
* *test_distinctUsers()* – Query the database to ensure the correct number of distinct users has been entered into the database.
* *test_time()* – Pass in three usernames and peaks to ensure the proper start time and end times have been logged in the database.
* *test_miles()* – Pass in three usernames and peaks to ensure the proper miles are returned for each is returned.
* *test_avHR()* – Pass in three usernames and peaks to ensure the correct avHR for each is returned.
* *test_steps()* - Pass in three usernames and peaks to ensure the correct steps taken by each user for each hike is returned.

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

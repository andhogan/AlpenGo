# Database Visual
![Database Design](https://user-images.githubusercontent.com/104743365/199325220-3112257c-4322-4e7c-8f99-c092316cd203.JPG)

# Table and Test Descriptions

## Table 1

### Table Name
  Peaks
### Table Description
  Database object to store all information related to each specific mountain peak listed on the website.
### Table Fields
  *PeakID (*Int*) – Unique identifier to identify each peak.
  *Name (*VarChar*) – The name of the mountain peak.
  *Location (*Float*, *Float*) – Latitude and Longitude of the mountain peak.
  *StartElevation (*Int*) – The starting elevation of the peak trail in feet.
  *SummitElevation (*Int*) – The elevation at the mountain summit in feet.
  *ElevationGain (*Int*) – The total elevation gain during the hike.
  *Length (*Float*) – The total distance of the trail in miles.
  *AvTime (*Float*) – The average time to completion for all hikers in hours.
  *RouteType (*VarChar*) – A description of the type of trail for the peak.
  *Class (*Int*) – The difficulty of the hike.
  *Description (*VarChar*) – A description of the mountain peak and trail.
### List of Tests
  **test_numPeaks()* – Query the database to ensure the total count of distinct peaks is equal to 10.
  **test_peakNames()* – Pass in an array of peak names to ensure all peaks are stored in the database.
  **test_location()* – Pass in three peak names to ensure that their correct locations are returned.
  **test_elevation()* – Pass in three peak names to ensure that their starting, summit and elevation gains are returned correctly.
  **test_length()* – Pass in three peak names to ensure their correct length is returned.
  **test_avTime()* – Pass in three peak names to ensure their correct times are reported.
  **test_routeType()* – Pass in three peak names to ensure their correct route type is returned.
  **test_class()* – Pass in three peak names to ensure their correct classes are returned.
  **test_description()* – Pass in three peak names to ensure their correct description is returned.

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

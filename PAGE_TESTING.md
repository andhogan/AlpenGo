You will create a list of descriptions for the pages that will be implemented for your project.
You must add a file PAGE_TESTING.md to your repository and provide the following for each page (at least 5 independent pages):


Page Title 

Page Description (include a mockup or hand drawn image of the page)

Parameters needed for the page

Data needed to render the page

Link destinations for the page

List of tests for verifying the rendering of the page

___
### About Page

###### Page Description
The about page describes the website, the project, the team members.
![About page drawing](https://user-images.githubusercontent.com/63213386/196829114-58d79715-069d-43e9-9b1e-c21ec0b7c9db.jpg)

###### Parameters needed for the page
N/A

###### Data needed to render the page
N/A - we will write our own information

###### Link destinations for this page
This page is accessed from anywhere on the site via the dropdown menu

###### List of tests for verifying the rendering of the page
Standard rendering of the page, much of this page is hard coded and implemented.

___
### Achievements Page

###### Page Description
This page details a user's acquired achievements. The page updates for the specific user as they acquire stats and complete trips. Achievements they've acquired should be colored in and positions at the top, while locked achievements will be grayed out. ![Achievements page drawing](https://user-images.githubusercontent.com/63213386/196830998-0add2e97-fdcd-48d3-b102-0cb0bd70856c.jpg)

###### Parameters needed for the page
Username, user logged in

###### Data needed to render the page
A many-to-many relationship table recording users and their achievements. A logged in user should be able to see the achievements they have acquired at the top of the page, and any that have not been unlocked will still remain grayed out. Users will also accumulate stats that will trigger acquisition of achievements

###### Link destinations for this page
Only users that are logged in should be able to see their own page via their User Profile portal

###### List of tests for verifying the rendering of the page
- Establish trigger to update user profile with achievement upon updating a stat
- Ensure users see their own user profile portal and subsequent achievement page
- Ensure achievements are organized and highlighted

___
### Peak Page Template

###### Page Description
Each Peak listed on the site will use this template to display information relating to the peak and input user data.  User data will be listed if the trail has already been hiked and logged.  The user can access the Hike Log page from this page to input user data for this specific peak.

![Peak Page Template](https://user-images.githubusercontent.com/104743365/196847877-b8e8e53e-783d-463e-a66e-eaf16d3ea619.JPG)

###### Parameters needed for the page
Peak selection passed from the Peak Selection page, user information for the user logged in, hiked completed flag indicating if the user has hiked the selected peak.

###### Data needed to render the page
Peak information including all trail information (i.e. class, elevations, length, etc…), image of peak and trailhead map, user stats for the peak pulled from database.

###### Link destination for this page
https://www.alpengo.com/peak

###### List of tests for verifying the rendering of the page
- Unit Test
  - test_peak – Ensure trail stats are correctly shown for the selected peak.
  - test_user_stats – Ensure user stats are displaying or null for the selected peak.
- Acceptance Test
  - Ensure information is properly displayed and in correct format.
  - Ensure Log Route can be selected.
- Integration Test
  - Ensure this page can be reached by the Peak Selection Page.  
  - Ensure clicking on Log Route reaches the Log Hike Page.

___
### Peak Selection Page

###### Page Description
This page will list all the trails available on the site, allowing the user to use a scroll bar to navigate through it.  Each peak will be separated by a row and will show a picture of the peak as well as the class, elevation, and length.  A column will indicate if the peak has already been logged or not.

![Peak Template](https://user-images.githubusercontent.com/104743365/196848463-8551ff1b-b726-4a67-8d93-e3d8e4e820f9.JPG)

###### Parameters needed for the page
User to know who is logged in to the site, Hike Completed Flag indicating if the trail has already been completed.

###### Data needed to render the page
Peak stats pulled from the database, user stats pulled from the database, images for each peak on the site.

###### Link destination for this page
https://www.alpengo.com/listpeaks

###### List of tests for verifying the rendering of the page
- Unit Test
  - test_climbed – ensure the Hike Completed Flag indicates the correct peaks for each user.
- Acceptance Test
  - Ensure the data is being formatted properly in an HTML table
  - Ensure the images are aligned with the correct peak.
  - Ensure the scroll bar works as intended.
- Integration Test
  - Ensure the page can be accessed from the Home Page.

___
### Log Hike Page

###### Page Description
This page will allow the user to input data to signal that the current peak has been hiked.  This will be a proxy method of simulating data capture by the AlpenGo system.  The user can input the date, starting time, and ending time of the hike, as well as the total miles, steps and average heart rate.

![Hikers Log Template](https://user-images.githubusercontent.com/104743365/196848837-c0f78b57-4276-467d-8b1c-044890e0b04c.JPG)

###### Parameters needed for the page
User to know who is logged in, Peak from Peak Page.

###### Data needed to render the page
User stats for the peak, user input.

###### Link destination for this page
https://www.alpengo.com/peak/input

###### List of tests for verifying the rendering of the page
- Unit Test
  - test_log – tests the submit button, ensuring the data is stored in the sql database properly.
  - test_peak – ensure the data is displayed correctly for each user
- Acceptance Test
  - Ensure information is displayed correctly in HTML table
  - Ensure window is centered on screen
  - Ensure Save Log button works as intended
- Integration Test
  - Ensure Save Log stores data
  - Ensure page can be accessed from the Peak Page

___
### Home Page
###### Page Description
This will be the page that shows upon first accessing the site. From here, the user can sign in, look at the peak list, look at their stats, and navigate to the about page. 

![Home Page Mockup](<img src="MacintoshHD/Users/user/Downloads/AlpenGo-Home_Page.jpg">)

###### Parameters needed for the page
Links to all transition pages, user information to display after log in, local information to display peaks near the user.

###### Data needed to render the page
Location information from user, user information from log in, image and information of peaks near the user.

###### Link destination for this page
About, Log In, Peaks, Stats, Contact/Help

###### List of tests for verifying the rendering of the page
  Make sure the correct information is displayed and in the correct format. 
	Ensure all transition links can be accessed.
	Make sure that the user’s name is displayed correctly after logging in.
___
### Login Page
###### Page Description
###### Parameters needed for the page
###### Data needed to render the page
###### Link destination for this page
###### List of tests for verifying the rendering of the page

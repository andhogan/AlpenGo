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

######
https://www.alpengo.com/peak

###### List of tests for verifying the rendering of the page
- Unit Test
- - test_peak – Ensure trail stats are correctly shown for the selected peak.
- - test_user_stats – Ensure user stats are displaying or null for the selected peak.
- Acceptance Test
- - Ensure information is properly displayed and in correct format.
- - Ensure Log Route can be selected.
- Integration Test
- - Ensure this page can be reached by the Peak Selection Page.  
- - Ensure clicking on Log Route reaches the Log Hike Page.




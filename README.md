# final-project
Web Programming with Python and JavaScript
Michael Blodgett
5/12/2019

Wander is a web app which allows users to create and share maps marked with locations they have been to or would like to go to. Visitors may search for users and view their maps (if they are set to public). Visitors may also create an account which allows them to make their own map. A user can make their map public or private (there is a "friends only" option but it isn't implemented yet. Currently it is the same as private) and can add markers to their map. Wander is hosted on heroku at:
https://wanderbeta.herokuapp.com/

Wander is a redesign and expansion on my cs50 project:
https://mapyourtravel.herokuapp.com/

Changes from previous version:
-The entire app has been rewritten from the ground up as a django application. It now uses the django User model and custom models for places and settings.
-The app is now connected to a heroku postgres database rather than a local database.
-All pages from MapYourTravel were condensed into a single 'user' page which is responsive to privacy settings and allows editing by the user whose page it is. 
-A good amount of javascript and css was added to enhance the UI and design.
-Users can no longer add a rating to a place.
-Users must now flag a place as visited, lived in, want to visit, or other.
-Places show different pins based on their flag.
`Index page added with a user search feature which uses javascript to auto populate possible matches.

Changes I would have liked to make if I had a little more time:
-Better error handling
-Mark, delete and privacy use javascript to make changes without refreshing page
-Friends list/system
-Comment on other users' profiles and/or places
-Filter by flag type

VIEWS.PY:
index
Renders the "index.html" page that loads with the default route and populates it with a list of all users for index.html's autocomplete.

view_user
Renders "user.html" which shows the user's map. It populates the page with the user's information as well as a flag which indicates if the user is viewing their own profile (shows editing options) and if the user is being redirected from adding a new location (zooms in on the new marker).

delete
Deletes a place object and redirects to view_user.

mark
Creates a new place object with all relevant data, sets the new place flag, and redirects to view_user.

privacy
Changes the user's privacy setting and redirects to view_user.

appregister
Renders the register.html page for a get request or creates a new user for a post request.

applogin
Renders the login.html page for a get request or logs in a user for a post request.

applogout
Logs out the current user.

TEMPLATES:

base.html
Contains the bootstrap navbar. Also links all html pages to styles.css and various outside scripts and stylesheets (honestly I'm not sure if everything here is being used, I didn't have a chance to go through and clean it up).

index.html
Contains the main page header as well as a searchbox and js to populate a list with links to profiles as a user types in the searchbox.

user.html
There's a lot going on here... Depending on who is looking at the page it renders a map, list of places, privacy setting and option to add new markers. It uses javascript to initialize the map, populate it with markers, show the user's current privacy setting, autocomplete with google maps api and expand/collapse additonal options for markers. This file is pretty huge. I would like to factor out more of the javascript, but I found that many of it didn't work when I linked it rather than keeping it in the html file.

register.html
Simple registration page.

Login.html
Simple login page.

STATIC:
mountains.png
Header image. Royalty free from:
 https://www.pexels.com/photo/adventure-alpine-background-black-and-white-355747/
Edited lightly in gimp

styles.css
Some basic css to define map size, form styles and the appearence of the header image

user.js
Contains a few functions I was able to factor out of user.html. Activates the google places autocomplete, the expand/collapse details button, and imports a function I lifted from stackoverflow which posts a form submission from js.

# Project Plan: 
## "Stylized Weather" 
 - An interactive weather site with dynamic weather system to show real time data of climate, temperature, time, weather, and more.
 - Custom designs will be assigned to each type of weather, making a more fluid and connected theme on the website
 - Users will be able to input "opinions" about the weather when logged in
 - Looking to use 3 databases for login/signup, API, and opinions list
    
### Easter egg - same style, different job
    - Game rating - other group's shared API
    - similar style as rest of site
    - Journals and important links will be held here
   
    
### About Page - About the team
    - have our favorite weather
    - fun facts and images representing us through weather
    - contains personal quotes and information
     
 ### Sign up 
    - Login and create account to make your own weather on our site
    
 ### Making your own weather
    - Can create fake city name and ideal weather to display on the site
    - Same style/art as actual weather for current location
    
 ## Current Indivdual Focus:
  - Travis - Easter Egg
  - Paul - Designs for weather
  - Sam - Sign in page/About page
  - Wesley - Nav bar/approutes
  
-Blueprints:
  - app.py is login and logic - has secret route
  - Siteroutes.py - made to show all static HTML
  - apiroutes.py - made for all API information for other group
  - Blueprint is a way to break apart the routes
- Indivdual blueprint to-do:
  - Travis - everything with secret route
  - Paul - All API routes
  - Sam - Routes for pages of site
  - Wesley - Routes for static HTML
  
  # Dependencies - download to work

1. flask
2. flask-wtf
3. wtforms
4. flask-sqlalchemy
5. werkzeug
6. flask-login
7. email-validator


## Mini Lab
- For point 1 we wrote all of our new class & object code in the corresponding blueprint section
- On line 4 of the file we defined the class Info to hold data about ourselves. 
- class Info exsample:
    - class Info:
    - name = "Persons name"
    - lang = "Persons fav language"
    - desc="Short desc about person"
    - github="https://github.com/PersonsGithub"
- From this class we defined a variable to which we can access the different data pieces (object) info = Info()
- We then displayed the objects by passing them to the html using jinja and rendering them. (line 14)
- 1 wow that we had was using a link to display as a link in an anchor tag in the html.
    

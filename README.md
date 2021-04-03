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


 # Mini Lab
    
Paul - https://github.com/Paul-Bokelman/styledweather-python/commit/5caa57509d33f2e6e4f08dbdd4fe178897b5d983

For point 1 I wrote all of my new class & object code in my corresponding blueprint section (/paul)
On line 4 of the paul.py file I defined the class Info to hold data about myself. 
```class Info:
    name = "Paul"
    lang = "javascript"
    desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog."
    github="https://github.com/Paul-Bokelman"
 ```
3. From this class I defined a variable to which I can access the different data pieces (object) info = Info()
4. I then displayed the objects by passing them to the html using jinja and rendering them. (line 14)
5. 1 wow that I had was using a link to display as a link in an anchor tag in the html.

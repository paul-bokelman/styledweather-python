# Final Point Grading Justification
## Theme Section
 - 4 Interactables (+2) and Data Driven page justification with code  (+2): 
    * [Login/Signup](https://github.com/Paul-Bokelman/styledweather-python/blob/master/routes/team/auth.py#L1-L58) 
    * ![](/static/media/Interact.png)
        * Data driven page which stores user input into database. Data can be retrieved later to give access to dashboard of website.   
    * [Ideal weather user input](https://github.com/Paul-Bokelman/styledweather-python/blob/master/routes/team/auth.py#L76-L85) 
        * Data driven page which stores user's descriptions. Will be stored forever, and tells users what their ideal weather is.  
    * [Current weather search](https://github.com/Paul-Bokelman/styledweather-python/blob/master/routes/team/api.py#L8-L19)
        * Data driven page which uses API to tell weather and condition statistics. The statistics will be displayed on the page.
    * [Crossover team API interaction](https://github.com/Paul-Bokelman/styledweather-python/blob/master/routes/team/api.py#L51-L61)
        * Data driven page which accesses crossover team API. Select a user from the list, and find their "To Do" list from the API. 
  - Something fun/interesting on site! (+1)
    * User is able to find any weather information from ANYWHERE on the world. Feel free to explore each corner of the globe! 
  

## Individual Section
- 4 Individual labs (+4)
- 2 Technicals (+1)
- Each Individual Section: [Paul](https://fish.nighthawkcodingsociety.com/paul), [Sam](https://fish.nighthawkcodingsociety.com/sam), [Travis](https://fish.nighthawkcodingsociety.com/travis), [Wesley](https://fish.nighthawkcodingsociety.com/wesley)
- [Blueprint organization for individual areas](https://github.com/Paul-Bokelman/styledweather-python/blob/81050ce2e87bab58a690581f157ea59da9e94a61/app.py#L23-L34)
- Each page looks the same and is easy to navigate, and getting to each page is easy too.
![](static/media/dropdown.png)
- 5/5 Points

# Project Plan: 
## "Stylized Weather" 
 - An interactive weather site with dynamic weather system to show real time data of climate, temperature, time, weather, and more.
 - Custom designs will be assigned to each type of weather, making a more fluid and connected theme on the website
 - Users will be able to input "opinions" about the weather when logged in
 - Looking to use 3 databases for login/signup, API, and opinions list
    
### Crossover API - same style, different job
    - Todos - other group's shared API, make reminders!
    - similar style as rest of site, custom to API group
    - Crossover API will be held here
   
### About Page - About the team
    - have our favorite weather
    - fun facts and images representing us through weather
    - contains minilabs and bubble sorts
     
 ### Sign up 
    - Login and create account to make your own weather on our site and your ideal weather!
    
 ### Making your ideal weather
    - Can create fake city name and ideal weather to display on the site
    - Same style/art as actual weather for current location
    
 ## Current Indivdual Focus:
  - Travis - Crossover API
  - Paul - Making API
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

Wesley - https://github.com/Paul-Bokelman/styledweather-python/commit/0919676599208c94da8dd70bb90f844ac4954fbf 

```class Info:
    name = "Wesley"
    lang = "HTML"
    desc="My name is Wesley Chen. I like Python and the logic it requires. Comp Sci is an interesting topic to learn about, and I feel that I have really enjoyed my time here learning code. I play video games in my free time."
    github="https://github.com/WesleyChen1"
```
1. The class and object code was writen in the idividual file with the root: /wesley
2. Starting in line 4, the class named **Info** was defined. It is written to assigns 4 variables : name, lang, desc, and github
3. On line 10, the object is assigned. the object name is info and will be used later to create the outputs
4. The data is displayed by rendering the template. The data is first passed to individual.html and uses jinja templating (similar to navbars) to create identicle webpages for everyone, but with different individual information.
5. The WOW factor would be defining the object and moving the data from the object to another html file. This html file, which used jinja, would repeat and create the web pages identically to everyone elses.


Travis- https://github.com/Paul-Bokelman/styledweather-python/commit/0919676599208c94da8dd70bb90f844ac4954fbf
```name = "Travis"
    lang = "CSS"
    desc="My name is Travis Medley and I love CSS, I like to hangout with friend and play videogames in my free time. I like going to the gym and I currently do swim for DN."
    github="https://github.com/Travis4th"
```
1. The objects and the classes have their indivdual file name and teh root for mine is /travis
2. The class called INFO was definded and is showing 4 different variables for me. name, favorite language, description and github.
3. on line 10 the object is assigned and the name is info and will later create outputs.
4. The data is shown by rendering the template. The data goes through the indivdual.html and templates it in our indivadual page for each of us.
5. Our WOW is showing how we can define the object and put it into the template to display is on our indivdual pages.


Sam - https://github.com/Paul-Bokelman/styledweather-python/commit/0919676599208c94da8dd70bb90f844ac4954fbf
```name = "Sam"
    lang = "HTML/CSS"
    desc = "My name is Sam Koenig and I like to code in HTML and CSS. CSP is currently my favorite class because I get to be creative when making web pages."
    github = "https://github.com/samkoenig9"
```
1. My individual root is /sam for the objects and classes.
2. The Info class is defined and shows 4 variables that relate to different things about me: name, favorite language, description, and my github.
3. The object is assigned on line 10 and given the name Info.
4. The page is shown by rendering template. The data goes through individual.html and uses variables from our own files.
5. The WOW is us showing how to define objects and put them into the template on each individual page.

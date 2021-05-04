from flask import Blueprint, render_template
about_paul = Blueprint('about_paul', __name__)

class Info:
    name = "Paul"
    lang = "javascript"
    desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog."
    github="https://github.com/Paul-Bokelman"
info = Info()

@about_paul.route("/about_paul", methods=['GET','POST'])
def about_route():
    return render_template('about.html', name=info.name, lang=info.lang, desc=info.desc, github=info.github)
    

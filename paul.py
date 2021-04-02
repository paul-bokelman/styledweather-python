from flask import Blueprint, render_template
paul = Blueprint('paul', __name__)

class Info:
    name = "Paul"
    lang = "javascript"
    desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog."
    github="https://github.com/Paul-Bokelman"
    
info = Info()

@paul.route("/paul")
def paul_route():
    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github)
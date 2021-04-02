from flask import Blueprint, render_template
travis = Blueprint('travis', __name__)

class Info:
    name = "Travis"
    lang = "css"
    desc="My name is Travis Medley and I am a triplet. I Love to code in CSS and currently computer science is my favorite class because I have freedom to do creative things. When I'm bored I love to play video games with friends and now that I understand more code, we try to sometimes understand the code of the game."
    github="https://github.com/Travis4th"

    
info = Info()

@travis.route("/travis")
def travis_route():
    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github)
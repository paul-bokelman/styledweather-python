from flask import Blueprint, render_template
sam = Blueprint('sam', __name__)

class Info:
    name = "Sam"
    lang = "html/css"
    desc="My name is Sam Koenig and I like to code in HTML and CSS. CSP is currently my favorite class because I get to be creative when making web pages."
    github="https://github.com/samkoenig9"
    
info = Info()

@sam.route("/sam")
def sam_route():
    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github)
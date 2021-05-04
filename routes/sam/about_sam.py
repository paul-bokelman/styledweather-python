from flask import Blueprint, render_template
about_sam = Blueprint('about_sam', __name__)

class Info:
    name = "Sam"
    lang = "html/css"
    desc="My name is Sam Koenig and I like to code in HTML and CSS. CSP is currently my favorite class because I get to be creative when making web pages."
    github="https://github.com/samkoenig9"
info = Info()

@about_sam.route("/about_sam", methods=['GET','POST'])
def about_route():
    return render_template('about.html', name=info.name, lang=info.lang, desc=info.desc, github=info.github)
    

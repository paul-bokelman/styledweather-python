from flask import render_template, Blueprint

about_paul = Blueprint('about_paul', __name__)

class Info:
    name = "Paul"
    lang = "javascript"
    desc="I have a dog."
    github="https://github.com/Paul-Bokelman"
info = Info()

@about_paul.route("/about_paul", methods=['GET','POST'])
def about_route():
    return render_template('about.html', name=info.name, lang=info.lang, desc=info.desc, github=info.github)
    

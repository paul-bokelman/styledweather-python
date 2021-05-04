from flask import Blueprint, render_template
about_wesley = Blueprint('about_wesley', __name__)

class Info:
    name = "Wesley"
    lang = "HTML"
    desc="My name is Wesley Chen. I like Python and the logic it requires. Comp Sci is an interesting topic to learn about, and I feel that I have really enjoyed my time here learning code. I play video games in my free time."
    github="https://github.com/WesleyChen1"
info = Info()

@about_wesley.route("/about_wesley", methods=['GET','POST'])
def about_route():
    return render_template('about.html', name=info.name, lang=info.lang, desc=info.desc, github=info.github)
    

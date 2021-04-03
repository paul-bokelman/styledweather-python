from flask import Blueprint, render_template
wesley = Blueprint('wesley', __name__)

class Info:
    name = "Wesley"
    lang = "HTML"
    desc="My name is Wesley Chen. I like Python and the logic it requires. Comp Sci is an interesting topic to learn about, and I feel that I have really enjoyed my time here learning code. I play video games in my free time."
    github="https://github.com/WesleyChen1"
    
info = Info()

@wesley.route("/wesley")
def wesley_route():
    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github)
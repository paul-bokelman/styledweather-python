from flask import Blueprint, render_template
sam = Blueprint('sam', __name__)


@sam.route("/sam")
def sam_route():
    return render_template("indiviual.html", name="Sam", lang="HTML/CSS", desc="My name is Sam Koenig and I like to code in HTML and CSS. CSP is currently my favorite class because I get to be creative when making web pages.")
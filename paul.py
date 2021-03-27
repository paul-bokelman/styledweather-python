from flask import Blueprint, render_template
paul = Blueprint('paul', __name__)


@paul.route("/paul")
def paul_route():
    return render_template("indiviual.html", name="Paul", lang="javascript", desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog.")
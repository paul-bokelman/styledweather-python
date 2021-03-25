from flask import Blueprint, render_template
site = Blueprint('site', __name__)


@site.route("/secret")
def secret():
    return render_template("secret.html")
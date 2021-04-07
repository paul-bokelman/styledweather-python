from flask import Blueprint, render_template, request
import math 
site = Blueprint('site', __name__)

@site.route("/secret")
def secret():
    return render_template("secret.html")

@site.route("/alg", methods=['GET','POST'])
def alg():
    a = int(request.form.get("a", False))
    b = int(request.form.get("b", False))
    c_squared = a**2 + b**2
    c = math.sqrt(c_squared)
    return render_template("alg.html", output=c)
from flask import render_template, Blueprint, request
import requests

junction = Blueprint('junction', __name__)

@junction.route("/paul", methods=['GET', 'POST'])
def paul_junction(): 
    return render_template("junction.html", name='paul')

@junction.route("/sam", methods=['GET', 'POST'])
def sam_junction(): 
    return render_template("junction.html", name='sam')

@junction.route("/travis", methods=['GET', 'POST'])
def travis_junction(): 
    return render_template("junction.html", name='travis')

@junction.route("/wesley", methods=['GET', 'POST'])
def wesley_junction(): 
    return render_template("junction.html", name='wesley')

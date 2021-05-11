from flask import render_template, Blueprint, request
import requests as r
import json as j

api = Blueprint('api', __name__)

@api.route("/home", methods=['GET', 'POST'])
@api.route("/", methods=['GET', 'POST'])
def home():
    userLocation = request.form.get('location', 'san diego') # search
    x = r.get(f"http://api.weatherapi.com/v1/forecast.json?q={userLocation}", headers={"content-type":"text", "key":"25a4dc68b6974dde8af192821212203"}) #Fetch rest api data
    data = j.loads(x.content) #Fetch rest api data
    name = data.get("location").get("name")
    localtime = data.get("location").get("localtime")
    condition = data.get("current").get("condition").get("text")
    tempF = data.get("current").get("temp_f")
    tempC = data.get("current").get("temp_c")

    iCondition = request.form.get('condition')
    iTemp = request.form.get('temp')
    iDesc = request.form.get('desc')

    print(iCondition, iTemp, iDesc)
    return render_template("home.html", name=name, localtime=localtime, condition=condition, tempF=tempF, tempC=tempC) #Fetch rest api data
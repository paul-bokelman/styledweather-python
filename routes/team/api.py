from flask import render_template, Blueprint, request, jsonify
import requests as r
import json as j
from models import User, IdealWeather

api = Blueprint('api', __name__)

@api.route("/home", methods=['GET', 'POST'])
@api.route("/", methods=['GET', 'POST'])
def home():
    userLocation = request.form.get('location', 'san diego') # search
    x = r.get(f"http://api.weatherapi.com/v1/forecast.json?q={userLocation}", headers={"content-type":"application/json", "key":"25a4dc68b6974dde8af192821212203"}) #Fetch rest api data
    data = j.loads(x.content) #Fetch rest api data
    name = data.get("location").get("name")
    localtime = data.get("location").get("localtime")
    condition = data.get("current").get("condition").get("text")
    tempF = data.get("current").get("temp_f")
    tempC = data.get("current").get("temp_c")
    return render_template("home.html", name=name, localtime=localtime, condition=condition, tempF=tempF, tempC=tempC) #Fetch rest api data

@api.route('/get_ideal_weather/<query_user>', methods=['GET'])
def get_weather(query_user):
    for user in User.query.filter_by(username=query_user):
        iw = user.ideal_weather[0]
        return jsonify({'username': user.username, 'ideal_weather': {
        'date_added': iw.date_added,
        'condition':  iw.condition,
        'temp':  iw.temp,
        'desc': iw.desc,
        }})
    return 'Request failed, make sure user exists (case sensitive).', 404

@api.route('/all_users', methods=["GET"])
def all_users():
    user_list = User.query.all()
    users = []
    for user in user_list: 
        users.append({'id': user.id, 'name': user.username})
    response = jsonify({'all_users': users})
    return response, 200

@api.route('/all_ideal_weathers', methods=["GET"])
def aiw():
    iw_list = IdealWeather.query.all()
    iw = []
    for iws in iw_list: 
        iw.append({'id': iws.id, 'owner_id': iws.user_id, 'condition': iws.condition, 'temp': iws.temp, 'desc': iws.desc, 'date_added': iws.date_added})
    response = jsonify({'all_ideal_weathers': iw})
    return response, 200
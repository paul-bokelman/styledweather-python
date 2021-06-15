from flask import render_template, Blueprint, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import requests

from models import db, User, IdealWeather

auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data): 
				login_user(user, remember=form.remember.data)
				return redirect(url_for('auth.dashboard'))

		return redirect(url_for('auth.login'))

	return render_template('login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		# redirect to page when user is created
		return redirect(url_for('auth.login'))
		# return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
	return render_template('signup.html', form=form)

@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    record = False
    user = User.query.filter_by(username=current_user.username).first()
    user_weather = user.ideal_weather
    if user_weather:
        condition = user_weather[0].condition
        temp = user_weather[0].temp
        desc =user_weather[0].desc
        date =user_weather[0].date_added
        record = True
        return render_template('dashboard.html', name=current_user.username, condition=condition, temp=temp, desc=desc, date=date, record=record)
    else:
        return render_template('dashboard.html', name=current_user.username, record=record)

@auth.route('/handle_data', methods=['GET','POST'])
def handle_data(): 
    username = User.query.filter_by(username=current_user.username).first()
    condition = request.form.get("condition", 'sunny')
    temp = int(request.form.get("temp", '72'))
    desc = request.form.get("desc", 'A nice sunny day with no distractions.')
    iw = IdealWeather(condition=condition, temp=temp, desc=desc, author=username)
    db.session.add(iw)
    db.session.commit()
    return redirect(url_for('auth.dashboard'))

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('api.home'))
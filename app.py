from flask import Flask, render_template, url_for, request, redirect
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

from routes.paul import about_paul
from routes.paul import paul_bubblesort
from routes.paul import paul_minilab
from routes.sam import about_sam
from routes.sam import sam_bubblesort
from routes.sam import sam_minilab
from routes.travis import about_travis
from routes.travis import travis_bubblesort
from routes.travis import travis_minilab
from routes.wesley import about_wesley
from routes.wesley import learn_css
from routes.wesley import wesley_bubblesort
from routes.wesley import wesley_minilab
from routes.team.api_routes import api
from routes.team.site_routes import junction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXOf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
csrf = CSRFProtect(app)
csrf.init_app(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


app.register_blueprint(about_paul.about_paul)
app.register_blueprint(paul_bubblesort.paul_bubblesort)
app.register_blueprint(paul_minilab.paul_minilab)
app.register_blueprint(about_sam.about_sam)
app.register_blueprint(sam_bubblesort.sam_bubblesort)
app.register_blueprint(sam_minilab.sam_minilab)
app.register_blueprint(about_travis.about_travis)
app.register_blueprint(travis_bubblesort.travis_bubblesort)
app.register_blueprint(travis_minilab.travis_minilab)
app.register_blueprint(about_wesley.about_wesley)
app.register_blueprint(wesley_bubblesort.wesley_bubblesort)
app.register_blueprint(wesley_minilab.wesley_minilab)
app.register_blueprint(learn_css.learn_css)

app.register_blueprint(api)
app.register_blueprint(junction)


class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True) 
    email = db.Column(db.String(50), unique=True) 
    password = db.Column(db.String(80)) 
    ideal_weather = db.relationship('IdealWeather', backref='author')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class IdealWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.Integer)
    desc = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"IdealWeather('{self.condition}', '{self.temp}', '{self.desc}', '{self.date_added}')"


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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data): 
				login_user(user, remember=form.remember.data)
				return redirect(url_for('dashboard'))

		return redirect(url_for('login'))

	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		# redirect to page when user is created
		return redirect(url_for('login'))
		# return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
	return render_template('signup.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
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

@app.route('/handle_data', methods=['GET','POST'])
def handle_data(): 
    username = User.query.filter_by(username=current_user.username).first()
    condition = request.form.get("condition", 'sunny')
    temp = int(request.form.get("temp", '72'))
    desc = request.form.get("desc", 'A nice sunny day with no distractions.')
    iw = IdealWeather(condition=condition, temp=temp, desc=desc, author=username)
    db.session.add(iw)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('api.home'))

if __name__ == "__main__":
    app.run(debug=True)
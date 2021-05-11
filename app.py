from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from utils import RegistrationForm, LoginForm
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

app.register_blueprint(api)
app.register_blueprint(junction)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    ideal_weather = db.relationship('IdealWeather', backref='author', lazy=True)

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('api.home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('api.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
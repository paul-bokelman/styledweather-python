from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf.csrf import CSRFProtect

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
csrf = CSRFProtect(app)
csrf.init_app(app)

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



if __name__ == "__main__":
    app.run(debug=True)
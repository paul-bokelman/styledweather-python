from flask import Flask
from flask_wtf.csrf import CSRFProtect
from models import db
from routes.paul import about_paul, paul_bubblesort, paul_minilab
from routes.sam import about_sam, sam_bubblesort, sam_minilab
from routes.travis import about_travis, travis_bubblesort, travis_minilab
from routes.wesley import about_wesley,wesley_bubblesort, wesley_minilab, learn_css
from routes.team.api import api
from routes.team.auth import auth, login_manager
from routes.team.site import junction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXOf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JSON_SORT_KEYS'] = False
db.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.init_app(app)

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
app.register_blueprint(auth)


if __name__ == "__main__":
    app.run(debug=True)
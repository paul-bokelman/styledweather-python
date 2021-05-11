from flask import Blueprint, render_template
learn_css = Blueprint('learn_css', __name__)

@learn_css.route("/learn_css", methods=['GET','POST'])
def learn_css_route():
    return render_template('learn_css.html')
    

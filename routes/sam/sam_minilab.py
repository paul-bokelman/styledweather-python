from flask import Blueprint, render_template, request
import math
sam_minilab = Blueprint('sam_minilab', __name__)  

@sam_minilab.route("/sam_minilab", methods=['GET','POST'])
def minilab_route():
    class pathCylinder: 
        def __init__(self, r = 0, h = 0, v = 0):
            self._r = r
            self._h = h
            self._v = v

        def get_final(self):
            r = self._r
            h = self._h
            self._v = round(math.pi*(r**2)*h,2)
            return [r, h, self._v]

        def set_final(self, r, h):
            self._r = r
            self._h = h

    path = pathCylinder()
    path.set_final(int(request.form.get("r", 2)), int(request.form.get("h", 2)))
    value_array = path.get_final()
    r = value_array[0]
    h = value_array[1]
    v = value_array[2]
    return render_template("minilab.html", r=r, h=h, output=v, who="sam")
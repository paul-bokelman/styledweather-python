from flask import Blueprint, render_template, request
wesley_minilab = Blueprint('wesley_minilab', __name__)  

@wesley_minilab.route("/wesley_minilab", methods=['GET','POST'])
def minilab_route():
    class pp:
        def __init__(self):
            self._p = 0
            self._v = 0
            self._n = 0
            self._t = 0

        def setter(self, p, v, n, t):
            self._p = p
            self._v = v
            self._n = n 
            self._t = t

        def getter(self):
            p = self._p
            v = self._v
            n = self._n
            t = self._t
        
            if not bool(p) and not bool(v) and not bool(n) and not bool(t):
                p = False
                v = "1"
                n = "1"
                t = "1"

            if not bool(p):
                output = round((int(n) * 0.08206 * int(t)) / int(v), 3)
                return output
            
            if not bool(v):
                output = round((int(n) * 0.08206 * int(t)) / int(p), 3)
                return output

            if not bool(n):
                output = round((int(p) * int(v)) / (int(t) * 0.08206), 3)
                return output

            if not bool(t):
                output = round((int(p) * int(v)) / (int(n) * 0.08206), 3)
                return output

            else:
                output = "You are the mega dum dum"
                return output


    pvnrt = pp()
    pvnrt.setter(request.form.get("p", False),request.form.get("v", False),request.form.get("n", False),request.form.get("t", False))
    output = pvnrt.getter()
    return render_template("minilab.html", output=output, who="wesley")
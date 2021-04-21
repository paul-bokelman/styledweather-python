from flask import Blueprint, render_template, request
import math 
import cmath


site = Blueprint('site', __name__)

@site.route("/secret")
def secret():
    return render_template("secret.html")

@site.route("/alg", methods=['GET','POST'])
def alg():
    class pathAlg: 
        def __init__(self, a = 0, b = 0, c = 0):
            self._a = a
            self._b = b
            self._c = c

        def get_final(self):
            a = self._a
            b = self._b
            c = a**2 + b**2
            self._c = math.sqrt(c)
            return [a, b, self._c]

        def set_final(self, a, b):
            self._a = a
            self._b = b

    path = pathAlg()
    path.set_final(int(request.form.get("a", 2)), int(request.form.get("b", 2)))
    value_array = path.get_final()
    a = value_array[0]
    b = value_array[1]
    c = value_array[2]
    return render_template("alg.html", a=a, b=b, output=c)

@site.route("/cylinder", methods=['GET','POST'])
def cylinder():
    r = int(request.form.get("r", False))
    h = int(request.form.get("h", False))
    r_squared = r**2
    v = round(math.pi*r_squared*h,2)
    return render_template("cylinder.html", output=v)
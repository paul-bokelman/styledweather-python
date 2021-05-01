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
    return render_template("cylinder.html", r=r, h=h, output=v)

    r = int(request.form.get("r", False))
    h = int(request.form.get("h", False))
    r_squared = r**2
    v = round(math.pi*r_squared*h,2)
    return render_template("cylinder.html", output=v)

@site.route("/pvnrt", methods=['GET','POST'])
def pvnrt():
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
    return render_template("pv.html", output = output)


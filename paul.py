from flask import Blueprint, render_template
paul = Blueprint('paul', __name__)

class Info:
    name = "Paul"
    lang = "javascript"
    desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog."
    github="https://github.com/Paul-Bokelman"
    
info = Info()

@paul.route("/paul")
def paul_route():
    class bubbleSort:
        def __init__(self):
            self._list = []
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print ("Sorted array is:")
    for i in range(len(arr)):
        print ("%d" %arr[i])

    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github)
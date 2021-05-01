from flask import Blueprint, render_template, request
travis = Blueprint('travis', __name__)

class Info:
    name = "Travis"
    lang = "css"
    desc="My name is Travis Medley and I am a triplet. I Love to code in CSS and currently computer science is my favorite class because I have freedom to do creative things. When I'm bored I love to play video games with friends and now that I understand more code, we try to sometimes understand the code of the game."
    github="https://github.com/Travis4th"

info = Info()

@travis.route("/travis",methods=['GET', 'POST'])
def travis_route():
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    original = request.form.getlist('input_text[]')
    arr = [1, 2]
    if request.method != 'GET':
        if original[0].isnumeric():
            arr = [int(i) for i in original]
        else:
            arr = original
        bubbleSort(arr)
    return render_template("indiviual.html", name=info.name, lang=info.lang, desc=info.desc, github=info.github, original=original, sorted=arr, paul=False)
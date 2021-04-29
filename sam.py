from flask import Blueprint, render_template, request
sam = Blueprint('sam', __name__)

class Info:
    name = "Sam"
    lang = "html/css"
    desc="My name is Sam Koenig and I like to code in HTML and CSS. CSP is currently my favorite class because I get to be creative when making web pages."
    github="https://github.com/samkoenig9"
    
info = Info()

@sam.route("/sam", methods=['GET', 'POST'])
def sam_route():
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
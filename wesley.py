from flask import Blueprint, render_template, request
wesley = Blueprint('wesley', __name__)

class Info:
    name = "Wesley"
    lang = "HTML"
    desc="My name is Wesley Chen. I like Python and the logic it requires. Comp Sci is an interesting topic to learn about, and I feel that I have really enjoyed my time here learning code. I play video games in my free time."
    github="https://github.com/WesleyChen1"
    
info = Info()

@wesley.route("/wesley", methods = ["GET", "POST"])
def wesley_route():
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
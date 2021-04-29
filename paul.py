from flask import Blueprint, render_template, request
paul = Blueprint('paul', __name__)

class Info:
    name = "Paul"
    lang = "javascript"
    desc="I am Paul Bokelman and I really enjoy coding and making cool projects on the internet and solving problems. I also have a very adorable dog."
    github="https://github.com/Paul-Bokelman"
    
info = Info()

@paul.route("/paul", methods=['GET','POST'])
def paul_route():

    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    if request.method == 'GET':
        return render_template('indiviual.html', name=info.name, lang=info.lang, desc=info.desc, github=info.github, paul=True)
    else:
        input_values = request.form.getlist('input_text[]')
        checkbox_values = request.form.getlist('input_checkbox')
        if input_values[0].isnumeric():
            arr = [int(i) for i in input_values]
        else:
            arr = input_values
        bubbleSort(arr)
        print(arr)
        # output = bubbleSort(input_values)
        return render_template('results.html',
                               input_values = input_values,
                               checkbox_values = checkbox_values, output=arr)
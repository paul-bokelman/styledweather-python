from flask import render_template, request, Blueprint

paul_bubblesort = Blueprint('paul_bubblesort', __name__)

@paul_bubblesort.route("/paul_bubblesort", methods=['GET','POST'])
def bubblesort_route():
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    if request.method == 'GET':
        return render_template('bubblesort.html', paul=True)
    else:
        input_values = request.form.getlist('input_text[]')
        checkbox_values = request.form.getlist('input_checkbox')
        if input_values[0].isnumeric():
            arr = [int(i) for i in input_values]
        else:
            arr = input_values
    bubbleSort(arr)
    print(arr)
    return render_template('bubblesort.html', input_values=input_values, checkbox_values=checkbox_values, output=arr, paul=True, render_output=True)
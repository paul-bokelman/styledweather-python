
from flask import Blueprint, render_template, request
sam_bubblesort= Blueprint('sam_bubblesort', __name__)

@sam_bubblesort.route("/sam_bubblesort", methods=['GET','POST'])
def bubblesort_route():
    def bubbleSort(array):
        a = len(array)
        for b in range(a-1):
            for c in range(0, a-b-1):
                if array[c] > array[c+1] :
                    array[c], array[c+1] = array[c+1], array[c]

    original = request.form.getlist('input_text[]')
    arr = [1, 2]
    if request.method != 'GET':
        if original[0].isnumeric():
            arr = [int(i) for i in original]
        else:
            arr = original
        bubbleSort(arr)
    return render_template("bubblesort.html", original=original, sorted=arr, paul=False, template="sam")
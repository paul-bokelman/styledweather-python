
from flask import Blueprint, render_template, request
wesley_bubblesort= Blueprint('wesley_bubblesort', __name__)

@wesley_bubblesort.route("/wesley_bubblesort", methods=['GET','POST'])
def bubblesort_route():  
    def bubbleSort(list):
        length = len(list)
        for i in range(length-1):
            for m in range(0, length-i-1):
                if list[m] > list[m+1] :
                    list[m], list[m+1] = list[m+1], list[m]

    original = request.form.getlist('input_text[]')
    arr = [1, 2]
    if request.method != 'GET':
        if original[0].isnumeric():
            arr = [int(i) for i in original]
        else:
            arr = original
        bubbleSort(arr)
    return render_template("bubblesort.html", original=original, sorted=arr, paul=False, template = "wesley")

from flask import Blueprint, render_template, request
travis_bubblesort= Blueprint('travis_bubblesort', __name__)

@travis_bubblesort.route("/travis_bubblesort", methods=['GET','POST'])
def bubblesort_route():
    def bubbleSort(arr):
        count = len(arr)
        for u in range(count-1):
            for l in range(0, count-u-1):
                if arr[l] > arr[l+1] :
                    arr[l], arr[l+1] = arr[l+1], arr[l]

    original = request.form.getlist('input_text[]')
    arr = [1, 2]
    if request.method != 'GET':
        if original[0].isnumeric():
            arr = [int(i) for i in original]
        else:
            arr = original
        bubbleSort(arr)
    return render_template("bubblesort.html", original=original, sorted=arr, paul=False)

from flask import Blueprint, render_template, request
travis_bubblesort= Blueprint('travis_bubblesort', __name__)

@travis_bubblesort.route("/travis_bubblesort", methods=['GET','POST'])
def bubblesort_route():
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
    return render_template("bubblesort.html", original=original, sorted=arr, paul=False)
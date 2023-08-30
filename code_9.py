from flask import Flask, render_template, request
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)


@app.route("/predict")
def predict(str1, str2):
    first, second = len(str1), len(str2)
    dp_array = [[0 for j in range(second + 1)] for i in range(first + 1)]
    for i in range(first + 1):
        for j in range(second + 1):
            if i == 0:
                dp_array[i][j] = j
            elif j == 0:
                dp_array[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]
            else:
                dp_array[i][j] = 1 + min(dp_array[i - 1][j], dp_array[i][j - 1], dp_array[i - 1][j - 1])

    return dp_array[first][second]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        first_str = request.form.get('first_str')
        second_str = request.form.get('second_str')
        result = predict(first_str, second_str)

    return render_template('code_9.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

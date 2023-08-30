from flask import Flask, render_template, request
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)


@app.route("/predict")
def predict(height, weight, k_value):
    input_arr = [[158, 58], [158, 59], [158, 63], [160, 59], [160, 60], [163, 60], [163, 61], [160, 64], [163, 64], [165, 61], [165, 62], [165, 65], [168, 62], [168, 63], [168, 66], [170, 63], [170, 64], [170, 68]]
    size = ['M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']

    height = height
    weight = weight
    k_value = int(k_value)


    datasetHW = np.array(input_arr)
    size_arr = np.array(size)

    knn = KNeighborsClassifier(n_neighbors=k_value, metric='euclidean')
    knn.fit(datasetHW, size_arr)

    test = np.array([[height, weight]], dtype=np.float64)

    prediction = knn.predict(test)

    if prediction == 'M':
        prediction = "M"
    elif prediction =="L":
        prediction="L"

    return prediction

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        k_value = request.form.get('k_value')
        result = predict(height, weight, k_value)

    return render_template('code_10.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

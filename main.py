from flask import Flask, render_template, request, Response
import pickle
import numpy as np
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
from wsgiref import simple_server
import os

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/prediction", methods=['POST'])
@cross_origin()
def prediction():
    try:
        if request.method == 'POST':

            # Get the data from the POST request.
            engineNumber = request.form['engineNumber']
            sensor2 = request.form['sensor2']
            sensor3 = request.form['sensor3']
            sensor4 = request.form['sensor4']
            sensor6 = request.form['sensor6']
            sensor7 = request.form['sensor7']
            sensor8 = request.form['sensor8']
            sensor9 = request.form['sensor9']
            sensor10 = request.form['sensor10']
            sensor11 = request.form['sensor11']
            sensor12 = request.form['sensor12']
            sensor13 = request.form['sensor13']
            sensor14 = request.form['sensor14']
            sensor15 = request.form['sensor15']
            sensor17 = request.form['sensor17']
            sensor20 = request.form['sensor20']
            sensor21 = request.form['sensor21']


            # Convert the data into numpy array
            input = np.array([[engineNumber, sensor2, sensor3, sensor4, sensor6, sensor7, sensor8,
                            sensor9, sensor10, sensor11, sensor12, sensor13, sensor14, sensor15,
                            sensor17, sensor20, sensor21]])

            # Load the model from the pickle file
            model = pickle.load(open("model/model.pkl", 'rb'))

            # Make the prediction
            prediction = model.predict(input)

        return render_template('predict.html', prediction=prediction)

    except Exception as e:
        return Response("Error Occurred! %s" %e)
 

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
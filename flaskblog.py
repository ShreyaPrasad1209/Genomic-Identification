from flask import Flask, render_template, jsonify, request
# from flask_assets import Bundle, Environment
from werkzeug import secure_filename
import json
# import numpy as np
import pickle
app = Flask(__name__)
# js= Bundle('home.js', output='gen/main.js')
# from keras.models import load_model

# from tensorflow.keras.layers import Conv1D, Dense, MaxPooling1D, Flatten
# from tensorflow.keras.models import Sequential



@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html' )
# Load the model
# model = pickle.load(open('trained_model.h5','rb'))
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


  
# @app.route("/predict", methods=['POST'])
# def predict():
#    data = {
#             {
#                "latitude":-6.081689,
#                "longitude":145.391881
#             },
#             {
#                "latitude":-5.207083,
#                "longitude":145.7887
#             },
#             {
#                "latitude":-5.826789,
#                "longitude":144.295861
#             },
#             {
#                "latitude":-6.569828,
#                "longitude":146.726242
#             },
#             {
#                "latitude":-9.443383,
#                "longitude":147.22005
#             }
#       };

#    return render_template("home.html", data = json.dumps(data));
if __name__ == '__main__':
  app.run(debug=True)  

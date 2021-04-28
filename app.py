import os
import pickle
from flask import Flask
import numpy as np
from flask import Flask, render_template
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_bootstrap import Bootstrap

app = Flask(__name__)
CORS(app)
api = Api(app)

# Unpickle our model so we can use it!
if os.path.isfile("./RFmomomodelFitted.pkl"):
  model = pickle.load(open("./RFmomomodelFitted.pkl", "rb"))
else:
  raise FileNotFoundError
class Predict(Resource):
  def post(self):
    args = parser.parse_args()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/predict', methods=['POST' ])  
def home():
  College = request.form['College']
  Vehicle = request.form['Vehicle']
  Refrig = request.form['Refrig']
  Park = request.form['Park']
  Restaurant = request.form['Restaurant']
  RoomServ = request.form['RoomServ']
  Distance = request.form['Distance']
  Security = request.form['Security']
  CanPet = request.form['CanPet']
  Chart = request.form['Chart']
  arr = np.array([[College,Vehicle,Refrig,Park,Restaurant,RoomServ,Distance,Security,CanPet,Chart]]).astype("int").reshape(1, -1)
  print(arr)
  pred = model.predict(arr)
  return render_template('predict.html', data=pred) 

# @app.route('/cv')
# def cv():
# 	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)


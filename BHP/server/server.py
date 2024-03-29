from flask import Flask, jsonify, request
import util
app = Flask(__name__) #create a flask app

@app.route('/') #http://
def home():
    util.load_saved_artefacts()
    return 'Start a Flask server for Home Price Prediction'
    
@app.route('/hello')
def hello():
    return 'Hi'

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify(
        {
            'locations': util.get_location_names()
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft =  float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print('Start a Flask server for Home Price Prediction...')
    util.load_saved_artefacts()
    app.run(debug=True, port=5000, host='0.0.0.0')

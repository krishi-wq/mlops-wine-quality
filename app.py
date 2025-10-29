from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
import os

def create_app():
    app = Flask(__name__)
    
    # Load the trained model
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Store model as app config
    app.config['model'] = model
    
    return app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Convert to DataFrame
        features = pd.DataFrame([data])
        
        # Make prediction
        model = app.config['model']
        prediction = model.predict(features)
        
        return jsonify({
            'prediction': int(prediction[0]),
            'message': 'Quality rating predicted successfully'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

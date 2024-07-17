from flask import request, jsonify
import numpy as np
import cv2
from app import app
from recommend_comic import recommend_comic
from azure_classifer import azure_predict_image

@app.route('/user/<string:user_id>', methods=['GET'])
def fetch_user(user_id):
    recommendations = recommend_comic(user_id)
    if not recommendations:
        return jsonify({'message': 'User not found or no history available'}), 404
    return jsonify(recommendations)

@app.route('/azure_checking_image', methods=['POST'])
def azure_predict():
    image_file = request.files.get('image')
        
    if not image_file:
        return jsonify({'error': 'No image uploaded'}), 400
    
    try:
        prediction = azure_predict_image(image_file)
        if prediction < 6:
            return jsonify({'SFW': True, 'filename': image_file.filename}), 200
        else:
            return jsonify({'SFW': False, 'filename': image_file.filename}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
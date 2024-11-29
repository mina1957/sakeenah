from flask import Blueprint, request, jsonify
from flask_cors import CORS
from src import db
from src.models import Recitation
from src.services.speech_recognition import recognize_speech
from src.services.feedback_generator import generate_feedback
from werkzeug.utils import secure_filename
import os

bp = Blueprint('recitation', __name__, url_prefix='/recitation')
CORS(bp)  # Enable CORS specifically for this blueprint

@bp.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

@bp.route('/submit', methods=['POST', 'OPTIONS'])
def submit_recitation():
    if request.method == "OPTIONS":
        return jsonify({"msg": "ok"}), 200
        
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the file directly from request
        audio_content = audio_file.read()

        # Get the recognized text
        recognized_text = recognize_speech(audio_content)

        # Generate feedback
        correct_text = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"  # For testing
        feedback, accuracy, detailed_feedback = generate_feedback(recognized_text, correct_text)

        return jsonify({
            'message': feedback,
            'accuracy': accuracy,
            'details': detailed_feedback,
            'recognized_text': recognized_text
        })

    except Exception as e:
        print(f"Error processing audio: {str(e)}")  # Add server-side logging
        return jsonify({'error': str(e)}), 500
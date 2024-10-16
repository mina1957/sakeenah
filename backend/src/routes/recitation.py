from flask import Blueprint, request, jsonify
from src import db
from src.models import Recitation
from src.services.speech_recognition import recognize_speech
from src.services.feedback_generator import generate_feedback

bp = Blueprint('recitation', __name__, url_prefix='/recitation')

@bp.route('/submit', methods=['POST'])
def submit_recitation():
    data = request.json
    audio_data = data['audio_data']
    verse_id = data['verse_id']
    user_id = data['user_id']

    # Perform speech recognition
    recognized_text = recognize_speech(audio_data)

    # Generate feedback
    feedback, accuracy_score = generate_feedback(recognized_text, verse_id)

    # Save recitation
    recitation = Recitation(user_id=user_id, verse_id=verse_id, accuracy_score=accuracy_score)
    db.session.add(recitation)
    db.session.commit()

    return jsonify({'feedback': feedback, 'accuracy_score': accuracy_score})
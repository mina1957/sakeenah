from flask import Blueprint, jsonify
from src.models import Progress

bp = Blueprint('progress', __name__, url_prefix='/progress')

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_progress(user_id):
    progress = Progress.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'surah_id': p.surah_id,
        'verses_completed': p.verses_completed,
        'last_verse_recited': p.last_verse_recited,
        'last_recitation_date': p.last_recitation_date
    } for p in progress])
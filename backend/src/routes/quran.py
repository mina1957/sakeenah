from flask import Blueprint, jsonify
from src.models import Surah
from src.models import Verse

bp = Blueprint('quran', __name__, url_prefix='/quran')

@bp.route('/surahs', methods=['GET'])
def get_surahs():
    surahs = Surah.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'number': s.number, 'total_verses': s.total_verses} for s in surahs])

@bp.route('/surah/<int:surah_id>/verses', methods=['GET'])
def get_verses(surah_id):
    verses = Verse.query.filter_by(surah_id=surah_id).all()
    return jsonify([{'id': v.id, 'verse_number': v.verse_number, 'text': v.text, 'audio_url': v.audio_url} for v in verses])

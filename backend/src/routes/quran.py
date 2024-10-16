from flask import Blueprint, jsonify
from src.models import Surah, Verse

bp = Blueprint('quran', __name__, url_prefix='/api/quran')

@bp.route('/surahs', methods=['GET'])
def get_surahs():
    surahs = Surah.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'number': s.number, 'total_verses': s.total_verses} for s in surahs])

@bp.route('/surah/<int:surah_id>', methods=['GET'])
def get_surah(surah_id):
    surah = Surah.query.get_or_404(surah_id)
    return jsonify({'id': surah.id, 'name': surah.name, 'number': surah.number, 'total_verses': surah.total_verses})

@bp.route('/surah/<int:surah_id>/verses', methods=['GET'])
def get_verses(surah_id):
    verses = Verse.query.filter_by(surah_id=surah_id).order_by(Verse.verse_number).all()
    return jsonify([{'id': v.id, 'verse_number': v.verse_number, 'text': v.text} for v in verses])

@bp.route('/verse/<int:verse_id>', methods=['GET'])
def get_verse(verse_id):
    verse = Verse.query.get_or_404(verse_id)
    return jsonify({'id': verse.id, 'surah_id': verse.surah_id, 'verse_number': verse.verse_number, 'text': verse.text})
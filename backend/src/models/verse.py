from app import db

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surah_id = db.Column(db.Integer, db.ForeignKey('surah.id'), nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    audio_url = db.Column(db.String(200))
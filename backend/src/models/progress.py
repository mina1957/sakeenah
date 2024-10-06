from app import db

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    surah_id = db.Column(db.Integer, db.ForeignKey('surah.id'), nullable=False)
    verses_completed = db.Column(db.Integer, default=0)
    last_verse_recited = db.Column(db.Integer)
    last_recitation_date = db.Column(db.DateTime)
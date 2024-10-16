from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

class Surah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    total_verses = db.Column(db.Integer, nullable=False)

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surah_id = db.Column(db.Integer, db.ForeignKey('surah.id'), nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    audio_url = db.Column(db.String(200))

class Recitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    verse_id = db.Column(db.Integer, db.ForeignKey('verse.id'), nullable=False)
    accuracy_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    surah_id = db.Column(db.Integer, db.ForeignKey('surah.id'), nullable=False)
    verses_completed = db.Column(db.Integer, default=0)
    last_verse_recited = db.Column(db.Integer)
    last_recitation_date = db.Column(db.DateTime)
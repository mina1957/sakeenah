from app import db

class Surah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    total_verses = db.Column(db.Integer, nullable=False)

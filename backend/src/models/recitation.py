from app import db

class Recitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    verse_id = db.Column(db.Integer, db.ForeignKey('verse.id'), nullable=False)
    accuracy_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
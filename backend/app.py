from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sakeenah.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models
from src.models import User, Surah, Verse, Recitation, Progress

# Import routes
from src.routes import auth, quran, recitation, progress

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(quran.bp)
app.register_blueprint(recitation.bp)
app.register_blueprint(progress.bp)

if __name__ == '__main__':
    app.run(debug=True)
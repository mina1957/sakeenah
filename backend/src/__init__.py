from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sakeenah.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Import and register blueprints
    from .routes import auth, quran, recitation, progress
    app.register_blueprint(auth.bp)
    app.register_blueprint(quran.bp)
    app.register_blueprint(recitation.bp)
    app.register_blueprint(progress.bp)

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Basic CORS setup
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

# Rest of your configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sakeenah.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import routes
from src.routes import auth, quran, recitation, progress

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(quran.bp)
app.register_blueprint(recitation.bp)
app.register_blueprint(progress.bp)

if __name__ == '__main__':
    app.run(debug=True)
from app import app, db
from src.models import User, Surah, Verse, Recitation, Progress

print("Imported models:", User, Surah, Verse, Recitation, Progress)

with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Database tables created successfully.")

    # Verify tables were created
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)
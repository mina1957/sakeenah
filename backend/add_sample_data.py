from app import app, db
from src.models import User, Surah, Verse
from werkzeug.security import generate_password_hash

def add_sample_data():
    with app.app_context():
        # Add a sample user
        user = User(username="test_user", email="test@example.com", password_hash=generate_password_hash("password123"))
        db.session.add(user)

        # Add Surah Al-Fatiha
        surah = Surah(name="الفاتحة", number=1, total_verses=7)
        db.session.add(surah)

        # Add verses of Al-Fatiha in Arabic
        verses = [
            Verse(surah_id=1, verse_number=1, text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"),
            Verse(surah_id=1, verse_number=2, text="الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"),
            Verse(surah_id=1, verse_number=3, text="الرَّحْمَٰنِ الرَّحِيمِ"),
            Verse(surah_id=1, verse_number=4, text="مَالِكِ يَوْمِ الدِّينِ"),
            Verse(surah_id=1, verse_number=5, text="إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"),
            Verse(surah_id=1, verse_number=6, text="اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ"),
            Verse(surah_id=1, verse_number=7, text="صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ"),
        ]
        db.session.add_all(verses)

        db.session.commit()
        print("Sample data added successfully.")

if __name__ == "__main__":
    add_sample_data()
from src import create_app, db
from src.services.feedback_generator import generate_feedback, get_verse_text, normalize_arabic_text
from src.models import Verse

app = create_app()

def test_feedback():
    with app.app_context():
        # Ensure we have a verse in the database
        verse = Verse.query.first()
        if not verse:
            verse = Verse(surah_id=1, verse_number=1, text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
            db.session.add(verse)
            db.session.commit()
        
        correct_text = get_verse_text(verse.id)
        print(f"Original correct text: {correct_text}")
        print(f"Normalized correct text: {normalize_arabic_text(correct_text)}")
        
        # Test perfect recitation
        recognized_text = correct_text
        print(f"\nPerfect recitation - Original: {recognized_text}")
        print(f"Perfect recitation - Normalized: {normalize_arabic_text(recognized_text)}")
        feedback, accuracy = generate_feedback(recognized_text, correct_text)
        print(f"Perfect recitation - Feedback: {feedback}, Accuracy: {accuracy}")
        
        # Test good recitation (with one word missing)
        recognized_text = " ".join(correct_text.split()[:-1])
        print(f"\nGood recitation - Original: {recognized_text}")
        print(f"Good recitation - Normalized: {normalize_arabic_text(recognized_text)}")
        feedback, accuracy = generate_feedback(recognized_text, correct_text)
        print(f"Good recitation - Feedback: {feedback}, Accuracy: {accuracy}")
        
        # Test poor recitation (with half words missing)
        recognized_text = " ".join(correct_text.split()[:len(correct_text.split())//2])
        print(f"\nPoor recitation - Original: {recognized_text}")
        print(f"Poor recitation - Normalized: {normalize_arabic_text(recognized_text)}")
        feedback, accuracy = generate_feedback(recognized_text, correct_text)
        print(f"Poor recitation - Feedback: {feedback}, Accuracy: {accuracy}")

if __name__ == "__main__":
    test_feedback()
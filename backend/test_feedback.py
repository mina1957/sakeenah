from src import create_app, db
from src.services.feedback_generator import generate_feedback, get_verse_text, normalize_arabic_text
from src.models import Verse

app = create_app()

def print_feedback_results(scenario, recognized_text, correct_text):
    print(f"\n{scenario} - Original: {recognized_text}")
    print(f"{scenario} - Normalized: {normalize_arabic_text(recognized_text)}")
    general_feedback, accuracy, detailed_feedback = generate_feedback(recognized_text, correct_text)
    print(f"{scenario} - General Feedback: {general_feedback}")
    print(f"{scenario} - Accuracy: {accuracy:.2f}")
    if detailed_feedback:
        print(f"{scenario} - Detailed Feedback:")
        for feedback in detailed_feedback:
            print(f"  - {feedback}")
    else:
        print(f"{scenario} - No specific issues detected.")

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
        print_feedback_results("Perfect recitation", recognized_text, correct_text)
        
        # Test good recitation (with one word missing)
        recognized_text = " ".join(correct_text.split()[:-1])
        print_feedback_results("Good recitation", recognized_text, correct_text)
        
        # Test poor recitation (with half words missing)
        recognized_text = " ".join(correct_text.split()[:len(correct_text.split())//2])
        print_feedback_results("Poor recitation", recognized_text, correct_text)

        # Test with some incorrect words
        recognized_text = "بسم الله الرحيم الرحمن"  # Swapped last two words
        print_feedback_results("Incorrect word order", recognized_text, correct_text)

if __name__ == "__main__":
    test_feedback()
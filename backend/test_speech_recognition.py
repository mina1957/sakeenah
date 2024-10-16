import os
from src.services.speech_recognition import recognize_speech
from src.services.feedback_generator import generate_feedback, get_verse_text
from src import create_app, db
from src.models import Verse

app = create_app()

def test_speech_recognition():
    with app.app_context():
        # Ensure we have a verse in the database
        verse = Verse.query.first()
        if not verse:
            verse = Verse(surah_id=1, verse_number=1, text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
            db.session.add(verse)
            db.session.commit()
        
        correct_text = get_verse_text(verse.id)
        print(f"Correct text: {correct_text}")

        # Path to your audio file
        audio_file_path = "/Users/aminatasakho/Desktop/sakeenah/backend/basmallah_inaccurate.wav"

        with open(audio_file_path, "rb") as audio_file:
            content = audio_file.read()

        recognized_text = recognize_speech(content)
        print(f"Recognized text: {recognized_text}")

        feedback, accuracy = generate_feedback(recognized_text, correct_text)
        print(f"Feedback: {feedback}")
        print(f"Accuracy: {accuracy}")

if __name__ == "__main__":
    test_speech_recognition()
import os
from src.services.speech_recognition import recognize_speech
from src.services.feedback_generator import generate_feedback, get_verse_text
from src import create_app, db
from src.models import Verse

app = create_app()

def process_audio_file(file_path, correct_text):
    print(f"\nProcessing file: {file_path}")
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    recognized_text = recognize_speech(content)
    print(f"Recognized text: {recognized_text}")

    feedback, accuracy = generate_feedback(recognized_text, correct_text)
    print(f"Feedback: {feedback}")
    print(f"Accuracy: {accuracy:.2f}")

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

        # Paths to your audio files
        accurate_audio_path = "/Users/aminatasakho/Desktop/sakeenah/backend/basmallah_accurate.wav"
        inaccurate_audio_path = "/Users/aminatasakho/Desktop/sakeenah/backend/basmallah_inaccurate.wav"

        # Process accurate audio
        process_audio_file(accurate_audio_path, correct_text)

        # Process inaccurate audio
        process_audio_file(inaccurate_audio_path, correct_text)

if __name__ == "__main__":
    test_speech_recognition()
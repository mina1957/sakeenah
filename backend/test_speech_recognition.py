import os
from src.services.speech_recognition import recognize_speech
from src.services.feedback_generator import generate_feedback, get_verse_text
from src import create_app, db
from src.models import Verse
import pygame.mixer
import time

app = create_app()

def wait_for_user():
    input("Press Enter to continue...")

def play_audio(file_path):
    print(f"Playing: {file_path}")
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Wait for the audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Error playing audio file: {e}")
    finally:
        pygame.mixer.quit()

def process_audio_file(file_path, correct_text):
    print(f"\nProcessing file: {file_path}")
    
    # Play the audio file first
    print("\nPlaying audio file. Please listen...")
    play_audio(file_path)
    
    # Add a small pause after playing
    print("\nProcessing the audio...")
    time.sleep(1)

    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    recognized_text = recognize_speech(content)
    print(f"Recognized text: {recognized_text}")

    general_feedback, accuracy, detailed_feedback = generate_feedback(recognized_text, correct_text)
    print(f"General Feedback: {general_feedback}")
    print(f"Accuracy: {accuracy:.2f}")
    if detailed_feedback:
        print("Detailed Feedback:")
        for feedback in detailed_feedback:
            print(f"- {feedback}")
    else:
        print("No specific issues detected.")

    # Wait for user before continuing
    wait_for_user()

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

        print("\nStarting audio tests. Make sure your sound is on.")
        wait_for_user()

        # Process accurate audio
        process_audio_file(accurate_audio_path, correct_text)

        # Process inaccurate audio
        process_audio_file(inaccurate_audio_path, correct_text)

if __name__ == "__main__":
    test_speech_recognition()
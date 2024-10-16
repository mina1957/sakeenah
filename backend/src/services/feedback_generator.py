from src.models import Verse
import re

def normalize_arabic_text(text):
    # Remove diacritics and any non-Arabic characters
    return re.sub(r'[^\u0600-\u06FF\s]', '', text)

def generate_feedback(recognized_text, correct_text):
    # Normalize both texts
    normalized_recognized = normalize_arabic_text(recognized_text)
    normalized_correct = normalize_arabic_text(correct_text)

    print(f"Debug - Normalized recognized: {normalized_recognized}")
    print(f"Debug - Normalized correct: {normalized_correct}")

    # Split into words
    words_recognized = normalized_recognized.split()
    words_correct = normalized_correct.split()

    print(f"Debug - Words recognized: {words_recognized}")
    print(f"Debug - Words correct: {words_correct}")

    # Count correct words
    correct_words = sum(1 for r, c in zip(words_recognized, words_correct) if r == c)
    total_words = len(words_correct)

    print(f"Debug - Correct words: {correct_words}")
    print(f"Debug - Total words: {total_words}")

    accuracy_score = correct_words / total_words if total_words > 0 else 0

    if accuracy_score > 0.9:
        feedback = "Excellent recitation! Keep up the good work."
    elif accuracy_score > 0.7:
        feedback = "Good effort. Try to focus on proper pronunciation of all words."
    else:
        feedback = "Keep practicing. Focus on correct pronunciation and memorization."

    return feedback, accuracy_score

def get_verse_text(verse_id):
    verse = Verse.query.get(verse_id)
    return verse.text if verse else ""
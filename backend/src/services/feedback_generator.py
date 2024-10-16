from src.models import Verse

def generate_feedback(recognized_text, verse_id):
    verse = Verse.query.get(verse_id)
    correct_text = verse.text if verse else ""

    # Simple text comparison (This should be replaced with a more sophisticated algorithm)
    words_recognized = set(recognized_text.split())
    words_correct = set(correct_text.split())

    correct_words = len(words_recognized.intersection(words_correct))
    total_words = len(words_correct)

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
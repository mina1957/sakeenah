import re
from src.models import Verse
from difflib import SequenceMatcher

def normalize_arabic_text(text):
    # Remove diacritics (harakat) and any non-Arabic characters
    text = re.sub(r'[\u064B-\u065F\u0670]', '', text)  # Remove diacritics
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)  # Keep only Arabic characters and spaces
    return text.strip()

def get_word_differences(recognized_words, correct_words):
    differences = []
    for i, (rec_word, cor_word) in enumerate(zip(recognized_words, correct_words)):
        if rec_word != cor_word:
            differences.append((i, rec_word, cor_word))
    
    # Check if recognized text has extra words
    if len(recognized_words) > len(correct_words):
        for i in range(len(correct_words), len(recognized_words)):
            differences.append((i, recognized_words[i], None))
    
    # Check if recognized text is missing words
    elif len(recognized_words) < len(correct_words):
        for i in range(len(recognized_words), len(correct_words)):
            differences.append((i, None, correct_words[i]))
    
    return differences

def generate_feedback(recognized_text, correct_text):
    # Normalize both texts
    normalized_recognized = normalize_arabic_text(recognized_text)
    normalized_correct = normalize_arabic_text(correct_text)

    print(f"Debug - Original recognized: {recognized_text}")
    print(f"Debug - Normalized recognized: {normalized_recognized}")
    print(f"Debug - Original correct: {correct_text}")
    print(f"Debug - Normalized correct: {normalized_correct}")

    # Split into words
    words_recognized = normalized_recognized.split()
    words_correct = normalized_correct.split()

    print(f"Debug - Words recognized: {words_recognized}")
    print(f"Debug - Words correct: {words_correct}")

    # Get word differences
    differences = get_word_differences(words_recognized, words_correct)

    # Count correct words
    correct_words = len(words_correct) - len(differences)
    total_words = len(words_correct)

    print(f"Debug - Correct words: {correct_words}")
    print(f"Debug - Total words: {total_words}")

    accuracy_score = correct_words / total_words if total_words > 0 else 0

    # Generate detailed feedback
    detailed_feedback = []
    for index, rec_word, cor_word in differences:
        if rec_word is None:
            detailed_feedback.append(f"Missing word at position {index + 1}: '{cor_word}'")
        elif cor_word is None:
            detailed_feedback.append(f"Extra word at position {index + 1}: '{rec_word}'")
        else:
            detailed_feedback.append(f"Mispronounced word at position {index + 1}: Said '{rec_word}' instead of '{cor_word}'")

    if accuracy_score == 1.0:
        general_feedback = "Excellent recitation! Perfect match."
    elif accuracy_score > 0.9:
        general_feedback = "Excellent recitation! Keep up the good work."
    elif accuracy_score > 0.7:
        general_feedback = "Good effort. Try to focus on proper pronunciation of all words."
    else:
        general_feedback = "Keep practicing. Focus on correct pronunciation and memorization."

    return general_feedback, accuracy_score, detailed_feedback

def get_verse_text(verse_id):
    verse = Verse.query.get(verse_id)
    return verse.text if verse else ""
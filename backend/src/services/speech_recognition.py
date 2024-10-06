from google.cloud import speech

def recognize_speech(audio_data):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ar-SA",
    )

    response = client.recognize(config=config, audio=audio)

    return response.results[0].alternatives[0].transcript if response.results else ""

import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    """
    Convert text to speech in French.
    """
    engine = pyttsx3.init()
    # Set voice to French
    for voice in engine.getProperty('voices'):
        if 'french' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """
    Convert speech to text using the microphone, specifically for French.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        try:
            audio = recognizer.listen(source)
            # Recognize French speech
            return recognizer.recognize_google(audio, language="fr-FR")
        except sr.UnknownValueError:
            return "Je n'ai pas compris. Veuillez répéter."
        except sr.RequestError as e:
            return f"Erreur de service : {e}"

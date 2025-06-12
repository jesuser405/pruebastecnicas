#Install SpeechRecognition and PyAudio
#Install pyttsx3 with pip install pyttsx3

import speech_recognition  as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
# Initialize the text-to-speech engine
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language='es-ES')
    print(f"Has dicho,: {text}")
    return text.lower()
if 'amazon' in talk():
    engine.say("Que quieres comprar en Amazon?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.amazon.es/s?k={text}")
elif 'youtube' in talk():
    engine.say("Que quieres buscar en YouTube?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
elif 'google' in talk():
    engine.say("Que quieres buscar en Google?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.google.com/search?q={text}")
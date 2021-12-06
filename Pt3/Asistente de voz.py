import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("voice", "spanish")

engine.say("Estoy apunto de decir la palabra con n; ayeye")
engine.runAndWait()

r = sr.Recognizer

with sr.Microphone() as source:
    print("Estas hablando")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-ES")
    print(text)


import speech_recognition as sr

filename = "sample.wav"

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
     audio_data = r.record(source)
     text = r.recognoze_google(audio_data)
     print(text)

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'fid' in command:
            print(command)

except:
    pass
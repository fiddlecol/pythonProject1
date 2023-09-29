import speech_recognition as aud

# fetch audio from devices microphone
# and store in variable reference of type speech_recognition
a = aud.Recognizer()

# declaring device microphone as the source to take audio input
with aud.Microphone() as source:
    print("Say something!")


# variable audio prints what user said in text format the end
audio = a.listen(source)

# invoking sphinx for speech recognition
try:
    # printing audio
    print("You said " + a.recognize_sphinx(audio))

except aud.UnknownValueError:
    # if the voice is unclear
    print("Could not understand")

except aud.RequestError as e:
    print("Error; {0}".format(e))

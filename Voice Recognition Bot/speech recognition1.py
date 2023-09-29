# importing LiveSpeech
from pocketsphinx import LiveSpeech

speech = LiveSpeech(keyphrase='forward', kws_threshold=1e-20)

# a for in loop to iterate in speech
for phrase in speech:
    # printing if the keyword is spoken with segments alongside.
    print(phrase.segments(detailed=True))


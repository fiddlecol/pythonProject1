import moviepy.editor as mp
import speech_recognition as sr

# Load the video
video = mp.VideoFileClip("254793680830_status_05384053fd824337b50a60f5d9a4812e")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("254793680830_status_05384053fd824337b50a60f5d9a4812e")

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("254793680830_status_05384053fd824337b50a60f5d9a4812e.wav") as source:
	data = r.record(source)

# Convert speech to text
text = r.recognize_google(data)

# Print the text
print("\nThe resultant text from video is: \n")
print(text)

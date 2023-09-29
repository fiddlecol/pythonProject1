import assemblyai as aai
import constants
aai.settings.api_key = constants.API_KEY

transcriber = aai.Transcriber()
transcript = transcriber.transcribe("")
print(transcript.text)

# Use AssemblyAI
import assemblyai as aai
# API token
aai.settings.api_key = "9255b525203241d2885b34578043a174"

# Create a transcriber object
transcriber = aai.Transcriber()

#setting file or URL link for what to transcribe
Audio_File = "TesterAudio1.wav"
transcript = transcriber.transcribe(f"{Audio_File}")
# For transcribing URL link instead of local file
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")

# After the transcription is complete, the text is printed out to the console.
print(transcript.text)
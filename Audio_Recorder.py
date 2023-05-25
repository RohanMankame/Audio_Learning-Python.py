import pyaudio
import wave

# Setting values for pyaudio parameters
Frame_per_buffer = 3000
Format = pyaudio.paInt16
Channels = 1
FrameRate = 10000

p = pyaudio.PyAudio()

Audio_DATA = p.open(
    format=Format,
    channels=Channels,
    rate=FrameRate,
    input=True,
    frames_per_buffer=Frame_per_buffer
)

print("RECORDING APP")
frames = []
seconds = input("Please input the length of time you would like to record for in seconds: ")
print("Recording starting now")
# LOOPS AND SETS DATA FOR RECORDING DEPENDING ON SECONDS AND PARAMETERS
for i in range(0, int(FrameRate / Frame_per_buffer * int(seconds))):
    data = Audio_DATA.read(Frame_per_buffer)
    frames.append(data)
# STOP AND CLOSE RECORDING
Audio_DATA.stop_stream()
Audio_DATA.close()
p.terminate()
print("Recording ended")

#SAVING THE AUDIO CLIP
obj = wave.open("Output.wav", "wb")
obj.setnchannels(Channels)
obj.setsampwidth(p.get_sample_size(Format))
obj.setframerate(FrameRate)
obj.writeframes(b"".join(frames))
obj.close()

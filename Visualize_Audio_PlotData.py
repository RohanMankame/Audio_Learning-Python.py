import wave
import matplotlib.pyplot as plt # for creating plot
import numpy as np
from playsound import playsound # for playing audio

# set the audio file we want to use
Audio_File = "StarWars60.wav"

# play the audio file, block = False allows the program to continue with the audio playing
playsound(f"{Audio_File}", block=False)

# open audio file to use it
obj = wave.open(f"{Audio_File}", "rb")

# getting values of the audio file
Sample_Frequency = obj.getframerate()
n_Samples = obj.getnframes()
signal_wave = obj.readframes(-1)

# Close the audio file
obj.close()


Time_Audio = n_Samples / Sample_Frequency

print("Audio is " +str(Time_Audio) + " seconds long")
# create an array of signal values using the signal wave
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
# creating linespace
times = np.linspace(0, Time_Audio, num=n_Samples)
# -----------------------------------------------------------------
# CREATING THE PLOT
# -----------------------------------------------------------------
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, Time_Audio)
plt.show()




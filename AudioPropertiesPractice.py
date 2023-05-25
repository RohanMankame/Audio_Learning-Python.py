import wave
# ---------------------------------------------------------------------------------
# !!!USE THIS EXTRA CODE FOR WAV FILES THAT GET "wave.Error: file does not start with RIFF id" ERROR!!!#
# this reconverts the wav file to wav file but with RIEF
# import librosa
# import soundfile as sf

# x,_ = librosa.load("TesterAudio1.wav",sr=16000)
# sf.write("TesterAudio.wav",x,16000)
# ------------------------------------------------------------------------------------
# FOR READING/Getting Info OF AUDIO FILE, CAN ONLY BE USED FOR .WAV FILES DUE TO USING PYTHONS INBUILT WAVE TOOLS
# ------------------------------------------------------------------------------------

obj = wave.open("StarWars60.wav", "rb")  # (file name, rb = read binary)

print("Num of Channel: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("parameters: ", obj.getparams())

Time_Audio = obj.getnframes() / obj.getframerate()
print("Audio clip length is: " + str(Time_Audio) + " seconds long")



#frames = obj.getnframes() / obj.getframerate()
obj.close()  # close the file object
# ---------------------------------------------------------------------------------------
# FOR SETTING/EDITING AUDIO FILE - BUT BE CAREFUL YOU CAN EASILY DAMAGE THE FILE
# ---------------------------------------------------------------------------------------
#obj_New = wave.open("StarWars60.wav","wb") #(file name, write binary)
#obj_New.setnchannels(1)
#obj_New.setsampwidth(2)

#obj_New.writeframes(frames)
# obj_New.setframerate()
# obj_New.setnframes()
# obj_New.setparams()

#obj_New.save("testeroutput.wav")
# os.open("testeroutput.wav")
obj.close()

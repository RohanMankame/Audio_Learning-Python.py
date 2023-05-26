import os
from gtts import gTTS

if __name__ == '__main__':
    language = 'en'
    print("Welcome to text to speach program by Rohan Mankame, A mp3 file will be generated from your prompt")
    print("Input prompt 'Quit Program' to exit")
    while True:
        x = input("Enter text prompt:")
        if x == "Quit":
            print("program exiting sequence initiated")
            break
        output = gTTS(text=x, lang=language, slow=False)
        output.save("output.wav")
        os.system("start output.wav")
from pygame import mixer
from gtts import gTTS

def main():
    print("Hello there testing")
    tts = gTTS("This is a test.  We are going to be creating an mp3 file with these words in it")
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()


if __name__ == '__main__':
    main()
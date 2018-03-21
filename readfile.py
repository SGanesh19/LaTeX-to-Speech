from gtts import gTTS
from speak import tts

def readfile(path):
    try:
        print("Building text to speech system")

        print ("Opening and closing a file.")
        #text_file = open(path,"r")
        #text_file.close()

        text_file = open(path,"r")
        lines = text_file.readlines()
        print(lines)
        for line in lines:
            lang = 'en'
            tts(line,lang)
            text_file.close()
    except Exception as e:
        print (e)

def readtxt(data):
    try:
        lang = 'en'
        tts(data, lang)
    except Exception as e:
        print(e)
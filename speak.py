from gtts import gTTS
import pyglet
import time
import os

def tts(text):
    try:
        file = gTTS(text=text, lang='en')
        filename = 'temp/temp.mp3'
        file.save(filename)

        music = pyglet.media.load(filename, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(filename)
    except Exception as e:
        print(e)

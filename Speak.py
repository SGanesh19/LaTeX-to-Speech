from gtts import gTTS
import pyglet
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
import time,os

def tts(text, lang):
    filename = 'G:/LaTex/ALLTRYS/Newtry1/temp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)

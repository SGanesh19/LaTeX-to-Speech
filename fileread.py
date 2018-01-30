import speech_recognition as sr
import webbrowser as wb
import speak
def rf(str):
    try:
        print("Building text to speech system")

        print("Opening and closing a file.")
        text_file = open("G:/LaTex/TeXmakerprj/try.pdf", "r")
        text_file.close()
        print("Opening a pdf file")
        text_file = open("G:/LaTex/TeXmakerprj/try.pdf", "r")
        lines = text_file.readlines()
        for line in lines:
            lang = 'en'
            speak.tts(line, lang)
            text_file.close()
    except Exception as e:
        print(e)


from Speak import tts
#This performs reading file operation
def rf():
    try:
        print("Building text to speech system")

        print("Opening and closing a file.")
        text_file = open("G:/LaTex/ALLTRYS/Newtry1/S/Outputdoc.txt", "r")
        text_file.close()

        text_file = open("G:/LaTex/ALLTRYS/Newtry1/S/Outputdoc.txt", "r")
        lines = text_file.readlines()
        print(lines)
        for line in lines:
            # line =line.replace('\n',' ')
            lang = 'en'
            tts(line, lang)
            text_file.close()
    except Exception as e:
        print(e)

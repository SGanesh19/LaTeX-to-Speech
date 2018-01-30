import re
#from gtts import gTTS
def latextolist(InputLatex):
    InputLatex = InputLatex.replace('\\{', '\\curlyopen')
    InputLatex = InputLatex.replace('\\}', '\\curlyclose')
    InputLatex = InputLatex.replace('{', ' ')
    InputLatex = InputLatex.replace('}', ' ')
    Input = InputLatex.replace('\\', ' ')
    data = Input.split(' ')
    return data
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    #print("str1:"+string1)
    #print("str2:"+string2)
    #print("from lsf"+" "+string1+"\n")
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    #print(answer.__len__())
    if(answer.__len__()>=3):
         return answer
    else:
        return '@'
def display(str,match):
    print(match)
    if (match):
        str = re.sub('to the superscript of', 'to', str, 1)
    print(str)
    #play(str)
#def play(str):
     #tts = gTTS(str, lang='en')
     #tts.save("E:\project\project_latex4.mp3")
    # os.system("mpg321 project_latex.mp3")
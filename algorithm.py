import re
import dict2
from collections import deque
from gtts import gTTS
import pyglet
#from S import speak
import speak
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
import time,os
queue = deque([])
#-----------------------------------------------------------------------------------------------------------------------
class algorithm:

    def __init__(self):
       first = " "
       second = " "
       finalstr= " "

    def generate(self, input):
        print(" ")
        print(queue)
        first = queue.popleft()
        second = queue.popleft()
        print(input)
        finalstr = first + " " + input + " " + second
        queue.appendleft(finalstr)
        return finalstr

#-----------------------------------------------------------------------------------------------------------------------
#def try1():
 #   inputstr = "{a}\+{b}\div{c}"
  #  for equ in inputstr:
   #    # for '\\' in equ:
    #        if equ in dic2.Operator:
     #           str = dict2.Operator.get(equ)
      #      if equ not in dict2.Operator:
       #         queue.append(equ)
        #        if queue.__len__()==2:
         #           result = algorithm().generate()
#    print(result)
#-----------------------------------------------------------------------------------------------------------------------
def try3():
    regex = r"\{(.*?)\}"
    operat = r"\((.*?)\)"
    initial = r"begin{equation}(.*?)end{equation}"
    inputstr = '''begin{equation}
        {a+b*(c*b)}
         end{equation}'''
    result = " "
    interres = " "
    interres1 = " "
    interres2 = " "

    filter = re.finditer(initial, inputstr, re.MULTILINE | re.DOTALL)



    for matchNum, match in enumerate(filter):
        for groupNum in range(0, len(match.groups())):
            interres =match.group(1)
            print(interres)
    matches = re.finditer(regex, interres, re.MULTILINE | re.DOTALL)
    for matchNum, match in enumerate(matches):
        for groupNum in range(0, len(match.groups())):
            interres1 =match.group(1)
            print(interres1)
    opmatch = re.finditer(operat, interres1, re.MULTILINE | re.DOTALL)
    for matchNum, match in enumerate(opmatch):
        for groupNum in range(0, len(match.groups())):
            interres2 = match.group(1)
            print(interres2)
            for line in interres2:
                for equ in line:
                    #equ = equ.replace('\\',' ')
                    if equ in dict2.Operation:
                        str = dict2.Operation.get(equ)
                        #print(str)
                        #queue.append(str)
                    #elif equ in dict2.Braces:
                     #   result = result+dict2.get(equ)
                    elif equ !=' ':
                        queue.append(equ)
                        #print(equ)
                        if queue.__len__() == 2:
                            result = algorithm().generate(str)

    print(result)

#-----------------------------------------------------------------------------------------------------------------------
def try2():
    #regex = r"\{(.*?)\}"
    operat =r"\w{3}"
    regex = r"begin{equation}(.*?)end{equation}"
    inputstr = '''begin{equation}
    {a+b*(c*b)}
     end{equation}'''
    result = " "
    interres = " "
    othstr= " "
    lang="en-uk"
    matches = re.finditer(regex,inputstr,re.MULTILINE | re.DOTALL)

    for matchNum, match in enumerate(matches):
        for groupNum in range(0,len(match.groups())):
            #interres =match.group(1)
            #opmatch = re.finditer(operat,interres,re.MULTILINE | re.DOTALL)
            #for matchNum, match in enumerate(opmatch):
                #for groupNum in range(0, len(match.groups())):
                    interres = match.group(1)
                    print(interres)
                    for line in interres:
                        for equ in line:
                            #equ = equ.replace('\\',' ')
                            if equ in dict2.Operation:
                                str = dict2.Operation.get(equ)
                                print(str)
                                #queue.append(str)
                            elif equ !=' ':
                                queue.append(equ)
                                print(equ)
                                if queue.__len__() == 2:
                                    result = algorithm().generate(str)

    #print(othstr)
    print(result)
    # speak.tts(result,lang)
#-----------------------------------------------------------------------------------------------------------------------

def power():
    InputLatex="x ^ 2"
    string = ""
    str = ""
    dictstr = ""
    Outcome = " "
    InputLatex.split(' ')
    print(InputLatex)
    match = re.match('sum_{.*?=.*?}\^{.*?}|prod_{.*?=.*?}\^{.*?}|int_{.*?}\^{.*?}', InputLatex)
    powerfuncmatch = "^"
    #powerfuncmatch = re.match('\\\\^', InputLatex)
    #basefuncmatch = re.match('\\\\_', InputLatex)
    # print(match)
    if(match):
        print("found")
    if (powerfuncmatch):
        #re.compile(powerfuncmatch)
        for equ in InputLatex:
            queue.append(equ)
            print(queue)
        if re.search(powerfuncmatch,InputLatex):
            InputLatex = re.replace(powerfuncmatch, 'to the power of', InputLatex)


    print("Now here")
    print(InputLatex)
#-----------------------------------------------------------------------------------------------------------------------
power()
#try2()
#try3()
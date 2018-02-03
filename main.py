from collections import deque
import  matchingstring
import dict
import re
from gtts import gTTS
queue=deque([])
string=""
str=""
dictstr=""
flag=0
class Inputspliter:
    def oneoperators(self, inputstr ):
        #why are u getting inputstr as input and printing 'input' ??? 
        print(input)
    def twoparameters(self, input):
        first=queue.popleft()
        second=queue.popleft()
        if input=='':
            finalstr=first+" "+second
        else:
          finalstr = first + " " + input + " " + second
        queue.appendleft(finalstr)
        return finalstr
def convert(InputLatex):
    #InputLatex=input("Enter the Latex format:")
    #Commented the unused string variables here 
    #string = ""
    #str = ""
    dictstr = ""
    #Outcome= " "
    match=re.match('sum_{.*?=.*?}\^{.*?}|prod_{.*?=.*?}\^{.*?}|int_{.*?}\^{.*?}',InputLatex)
    #powerfuncmatch = re.match('\w\^'|'\(.*?\)\^',InputLatex)
    #basefuncmatch = re.match('\w\_'|'\(.*?\)\_',InputLatex)
    #print(match)
    data=matchingstring.latextolist(InputLatex)
    for equ in data:
        if equ in dict.Relational:
             dictstr=dict.Relational.get(equ)
        elif equ !='':
            if(equ in dict.greekletters):
                 queue.append(dict.greekletters.get(equ))
            else:
                queue.append(equ)
            if queue.__len__()==2:
                 fs=Inputspliter().twoparameters(dictstr)
                 dictstr=''
                 match=matchingstring.longestSubstringFinder(str, fs)
                 if match in str:
                    str = str.replace(match,fs)
                 else:
                    str=str+" "+fs



    #matchingstring.display(str,match)
    #print('str before:'+str)
    if (match):
        pass
     #   print('in')
    str = re.sub('to the superscript of', 'to', str)
    #print(str)
    #if(powerfuncmatch):
     #   re.compile(powerfuncmatch)
      #  str = re.sub(powerfuncmatch,'to the power of',str)
    #Outcome constitutes of converted string which is returned to getEquation.py
    Outcome = str
    return Outcome



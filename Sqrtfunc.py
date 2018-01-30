#Importing the regular expression package
import re
from main import convert


#Importing the dictionary
import dict2

#Importing package for deque operation on the queue
from collections import deque
queue = deque([])

#Declarations
string = " "
str = " "

#Class
class squareroot:

    #This is initiated when the object of the sqrt is called
    def __init__(self):
        first = " "
        second = " "
        finalstr = " "
        string = " "
        result= " "
        intermediateResult = " "
        value= " "

    #Appending the stings to final string
    def sqrparameters(self,flag):
        print(queue)
        first = queue.popleft()
        second = queue.popleft()
        if flag == 0:
            i = 0
        else:
            i = 1
        #print(input)
        if i == 0:
            finalstr = second + "-th " + first
            queue.appendleft(finalstr)
        elif i == 1:
            finalstr = first + " " + second
            queue.appendleft(finalstr)
        return finalstr

        # Appending the stings to final string
    def norparameters(self):
        #print(queue)
        first = queue.popleft()
        second = queue.popleft()
        #print(input)
        finalstr = first + " " + second
        queue.appendleft(finalstr)
        return finalstr

    # This process is executed for the latex equation
    # of type \sqrt[\w]{\w}
    def sqrsub(self,temp):
        intermediateResult = " "
        result = " "
        temp = temp.replace('{', ' ')
        temp = temp.replace('}', ' ')
        temp = temp.replace('[', ' ')
        temp = temp.replace(']', ' ')
        input = temp.replace('\\', ' ')
        input = input.replace('sqrt', 'root of')
        data = input.split(' ')
        #print(data)
        #rec = 1
        Matchcurly =r"\{(.*?)\}"
        matches = re.finditer(Matchcurly, temp, re.MULTILINE | re.DOTALL)
        for matchNum,match in enumerate(matches):
            for groupNum in range(0,len(match.group())):
                intermediateResult=match.group(1)
                print(intermediateResult)
        value = convert(intermediateResult)
        print(value)
        itermediatestring = re.sub(intermediateResult,value,intermediateResult)
        flag = -2
        for equ in itermediatestring:
            if equ != '':
                queue.append(equ)
                #print(rec)
                #print(queue.__len__())
                if queue.__len__() == 2:
                    #print("flag="+'%d'%flag)
                    result = squareroot().sqrparameters(flag)
                #rec += 1
                flag += 1
        return result

        # This process is executed for the latex equation
        # of type \sqrt{\w}
    def nrsub(self,temp):
        temp = temp.replace('{', ' ')
        temp = temp.replace('}', ' ')
        temp = temp.replace('[', ' ')
        temp = temp.replace(']', ' ')
        input = temp.replace('\\', ' ')
        input = input.replace('sqrt', 'square root of')
        data = input.split(' ')
        #print(data)
        #rec = 1
        for equ in data:
            if equ != '':
                queue.append(equ)
                #print(rec)
                # print(queue.__len__())
                if queue.__len__() == 2:
                    result=squareroot().norparameters()
                #rec += 1
        return result

def sqrt_string_match():
    inputstr = "\sqrt[n]{x2+y2+z2+a2+b2+c2-h2}"
    if re.search("\\\\sqrt\[\w{1}\]", inputstr):
        result = squareroot().sqrsub(inputstr)
        print(result)
    elif re.search("\\\\sqrt", inputstr):
        result = squareroot().nrsub(inputstr)
        print(result)
    else:
        print("The input does not match with sqrt pattern")

#Initiation of execution process
sqrt_string_match()



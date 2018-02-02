#Importing the regular expression package
import re
from main import convert

#Importing package for deque operation on the queue
from collections import deque
queue = deque([])

#Declarations
string = " "
str = " "

#Class
class squareroot:

    #Appending the stings to final string
    def sqrparameters(self,flag):
        finalstr = " "
        #print(queue)
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
        temp = temp.replace('{', ' open curly braces ')
        temp = temp.replace('}', ' close curly braces ')
        temp = temp.replace('[', ' ')
        temp = temp.replace(']', ' ')
        input = temp.replace('\\', ' ')
        input = input.replace('sqrt', 'root of')
        data = input.split(' ')
        flag = -2
        for equ in data:
            if equ != '':
                queue.append(equ)
                if queue.__len__() == 2:
                    result = squareroot().sqrparameters(flag)
                flag += 1
        return result

    # This process is executed for the latex equation
    # of type \sqrt{\w}
    def nrsub(self,temp):
        result = " "
        temp = temp.replace('{', ' open curly braces ')
        temp = temp.replace('}', ' close curly braces ')
        temp = temp.replace('[', ' ')
        temp = temp.replace(']', ' ')
        input = temp.replace('\\', ' ')
        input = input.replace('sqrt', 'square root of')
        data = input.split(' ')
        for equ in data:
            if equ != '':
                queue.append(equ)
                if queue.__len__() == 2:
                    result=squareroot().norparameters()
        return result

    #This function is for matching the contents within the
    #Curly braces and returns the corresponding matched value
    def matchcurly(self,string):
        intermediateResult= " "
        sign =r"\{(.*?)\}"
        matches = re.finditer(sign,string, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.group())):
                intermediateResult = match.group(1)
        return intermediateResult

#The main execution of the program is initiated from this function
def sqrt_string_match():
    try:
        inputstr = "\sqrt{ x2 + y2 + z2 + a2 + b2 + c2 - h2 }"
        if re.search("\\\\sqrt\[\w{1}\]", inputstr):

            convertedvalue = " "
            matchedvaluevalue = " "
            matchedvalue = squareroot().matchcurly(inputstr)
            convertedvalue = convert(matchedvalue)
            inputstr = inputstr.replace(matchedvalue,convertedvalue)

            result = squareroot().sqrsub(inputstr)
            print(result)
        elif re.search("\\\\sqrt", inputstr):

            convertedvalue = " "
            matchedvaluevalue = " "
            matchedvalue = squareroot().matchcurly(inputstr)
            convertedvalue = convert(matchedvalue)
            inputstr = inputstr.replace(matchedvalue, convertedvalue)

            result = squareroot().nrsub(inputstr)
            print(result)
        else:
            print("The input does not match with sqrt pattern and the string does not follows the LaTeX syntax format")
    except Exception as e:
        print(e)

#Invoking of execution process
sqrt_string_match()



import re
from collections import deque
from readfile import readfile,readtxt
from main import convert

queue = deque([])
def getEqu_frmfile(path):
    try:
        result = " "
        value = 0
        Ouput_path = "output/Outputdoc.txt"
        intermediateResult= " "
        matchingTags = r"begin{equation}(.*?)end{equation}"
        #print("Opening a file...")
        Inputfile = open(path, "r")
        Inputstr = Inputfile.read()
        #print("Reading done")
        matches = re.finditer(matchingTags,Inputstr,re.MULTILINE | re.DOTALL)
        #print("Matching string")
        file_wr(Ouput_path, result)
        for matchNum, match in enumerate(matches):

            for groupNum in range(0, len(match.groups())):
                intermediateResult = match.group(1)

                file_write(Ouput_path, "Equation %d:" %(value + 1))
                print("intermediateResult:")
                print(intermediateResult)
                result = convert(intermediateResult)
                print("Result:")
                print(result)

                file_write(Ouput_path, result)
                value+=1
        Inputfile.close()
        #print(result)
        print("terminated reading mode")
        return result
    except Exception as e:
        print("Exception:")
        print(e)

def file_write(Output_path,value):
    try:
        #print("Writing file")
        Outputfile=open(Output_path, "a+")
        Outputfile.flush()
        Outputfile.write(value)

        #with open(Output_path, "w+") as Outputfile:
         #   Outputfile.write(value)
        #print("completed writing")
        Outputfile.close()
        #print("Process completed")
    except Exception as e:
        print("Exception:")
        print(e)

def file_wr(Output_path, value):
        try:
            print("Writing file")
            Outputfile = open(Output_path, "w")
            Outputfile.flush()
            Outputfile.write(value)

        except Exception as e:
             print("Exception:")
             print(e)
def getfrm_txtbox(Input):
    result = convert(Input)
    return result

def executetxt(Input):
    result = convert(Input)
    readtxt(result)
def executefile(path):
    Ouput_path = "output/Outputdoc.txt"
    result=getEqu_frmfile(path)
    readfile(Ouput_path)
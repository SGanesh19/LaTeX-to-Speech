import re
import os
import dict
from collections import deque
from readfile import readfile,readtxt
from main import convert
from Sqrtfix import sqrt_string_match
queue = deque([])
def getEqu_frmfile(path):
    try:
        result = " "
        intermediateResult= " "
        matchingTags = r"begin{equation}(.*?)end{equation}"
        print("Opening a file...")
        Inputfile = open(path, "r")
        Inputstr = Inputfile.read()
        print("Reading done")
        matches = re.finditer(matchingTags,Inputstr,re.MULTILINE | re.DOTALL)
        print("Matching string")
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                intermediateResult = match.group(1)
        result = convert(intermediateResult)
        print("Intermediate result:")
        print(intermediateResult)
        print("Result:")
        print(result)
        result=result.replace('\n',' ')
        Inputfile.close()
        #print(result)
        print("terminated reading mode")
        return result
    except Exception as e:
        print("Exception:")
        print(e)

def file_write(Output_path,value):
    try:
        print("Writing file")
        Outputfile=open(Output_path, "w")
        Outputfile.flush()
        Outputfile.write(value)

        #with open(Output_path, "w+") as Outputfile:
         #   Outputfile.write(value)
        print("completed writing")
        Outputfile.close()
        print("Process completed")

    except Exception as e:
        print("Exception:")
        print(e)
def getfrm_txtbox(Input):
    result = convert(Input)
    return result

def executetxt(Input):
    readtxt(Input)
def executefile(path):
    Ouput_path = "G:/LaTex/L2S13feb/Outputdoc.txt"
    #Input_path1 = "G:/LaTex/L2S13feb/Inputdoc.tex"
    result=getEqu_frmfile(path)
    file_write(Ouput_path,result)
    readfile(Ouput_path)
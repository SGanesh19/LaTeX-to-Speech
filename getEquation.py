import re
from collections import deque
from readfile import rf
from main import convert

queue = deque([])


def main():
    try:
        result = " "
        Inputstr = " "
        intermediateResult = " "
        matchingTags = r"begin{equation}(.*?)end{equation}"
        print("Opening a file...")
        # Inputfile = open("G:/LaTex/ALL TRYS/Newtry1/S/Inputdoc.tex", "r")
        # Inputfile.close()
        Inputfile = open("G:/LaTex/ALLTRYS/Newtry1/S/Inputdoc.tex", "r")
        Inputstr = Inputfile.read()
        print("Reading done")
        # path ="G:/LaTex/ALLTRYS/Newtry1/S/Inputdoc.tex"
        # Inputstr = rf(path)
        matches = re.finditer(matchingTags, Inputstr, re.MULTILINE | re.DOTALL)
        print("Matching string")
        # while (intermediateResult == 0):
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                intermediateResult = match.group(1)
                print(intermediateResult)
        result = convert(intermediateResult)
        # print(result)
        Inputfile.close()
        print("terminated reading mode")
        # print(result)
        print("Writing file")
        with open("G:/LaTex/ALLTRYS/Newtry1/S/Outputdoc.txt", "w") as Outputfile:
            Outputfile.write(result)
        print("completed writing")
        Outputfile.close()
        print("Process completed")
    except:
        print("error")


main()
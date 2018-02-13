from collections import deque
import dict
import producelatex
#import gtrail
import matchingstring
import geometry
queue=deque([])
queue1=deque([])
queue2=deque([])
queue3=deque([])
string=''
dictstr=' '
finalstr=' '
class Inputspliter:
   InputLatex=input("Enter the Latex format:")
   data = matchingstring.latextolist(InputLatex)
   for equ in data:
       if equ!='':
           if equ in dict.Rhs:
             queue2.append(dict.Rhs.get(equ))
           elif equ in dict.Underlines:
             queue3.append(dict.Underlines.get(equ))
   if queue2.__len__()!=0:
       finalstr=gtrail.specialfunction(InputLatex)
   elif queue3.__len__()!=0:
       geometry.Inputspliter1().parameters(data)
   else:
      data = producelatex.latextolist(InputLatex)
      for equ in data:
           if equ!=' ':
             if equ in dict.Special:
              queue.append(' ')
              queue.append(dict.Special.get(equ))
              queue.append(' ')
             else:
              queue.append(equ)
           else:
              queue.append(equ)
for element in queue:
     string=string+element
Input=string.split(' ')
for equation in Input:
        if equation!=' ':
          if equation in dict.Dictionary:
              queue1.append(dict.Dictionary.get(equation))
          elif equation in dict.Greekletters:
              queue1.append(dict.Greekletters.get(equation))
          elif equation in dict.Negationdbin:
              queue1.append(dict.Negationdbin.get(equation))
          elif equation in dict.Rhs:
              queue1.append(dict.Rhs.get(equation))
          else:
              queue1.append(equation)
for element1 in queue1:
    finalstr=finalstr+' '+element1
print(finalstr)
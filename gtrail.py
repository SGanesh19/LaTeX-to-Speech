from collections import deque
#import neccessary files
import dict
import producelatex
import separete
#import queues
queue=deque([])
queue1=deque([])
queue2=deque([])
#the method to process the special symbols(integral,fraction,product,summation)
def specialfunction(InputLatex):
    string=''
    finalstr=''
#to call the latexttolist method
    data = producelatex.latextolist(InputLatex)
    for equ in data:
          if equ!=' ':
             if equ in dict.Special1:
               queue.append(' ')
               queue.append(dict.Special1.get(equ))
               queue.append(' ')
             else:
                 queue.append(equ)
          else:
              queue.append(equ)
    for m in range(queue.__len__()):
           element = queue.popleft()
           string  = string + element
    Input=separete.addingElement(string)
    for equation in Input:
        if equation!=' ':
          if equation in dict.Dictionary:
              queue1.append(dict.Dictionary.get(equation))
          elif equation in dict.Greekletters:
              queue1.append(dict.Greekletters.get(equation))
          elif equation in dict.Accents:
              queue1.append(dict.Accents.get(equation))
          elif equation in dict.Negationdbin:
              queue1.append(dict.Negationdbin.get(equation))
          elif equation in dict.Rhs:
              queue1.append(dict.Rhs.get(equation))
          else:
              queue1.append(equation)
    for m in range(queue1.__len__()):
        element1=queue1.popleft()
        finalstr=finalstr+' '+element1
    return finalstr
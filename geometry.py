from collections import deque
#import Dictionary
import dict
#Intialize the queue
queue=deque([])
queue1=deque([])
dictstr=""
#Class
class Inputspliter1:
     #Covert LaTex to Readable Format
      def gparameters(self, input):
           first = queue.popleft()
           second = queue.popleft()
           if input == ' ':
                finalstr = second + " " + first
           else:
                finalstr = input + " " + second + " " + first
           queue1.append(finalstr)
      #Display the Latex Equivalent to Human Readable Format
      def display(self):
          string=" "
          for element in queue1:
              string=string+" "+element
          print(string)
     #If there is a geometry element present in data control must be transfered and further processed
      def parameters(self,data1):
            dictstr=""
            listlen=data1.__len__()
            for equ in data1:
                if equ in dict.Underlines:
                   queue.append(dict.Underlines.get(equ))
                elif equ != '':
                    if equ in dict.Dictionary:
                       dictstr = dict.Dictionary.get(equ)
                    elif equ in dict.Greekletters:
                       dictstr =dict.Dictionary.get(equ)
                    else:
                        queue.append(equ)
                if queue.__len__() == 2:
                  fs = Inputspliter1().gparameters(dictstr)
            if(listlen==data1.__len__()):
                 fs = Inputspliter1().display()
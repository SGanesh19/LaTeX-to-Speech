#method to append "by"
def addingElement(string):
    i=2
    Input=string.split(' ')
    length=len(Input)
    for element in Input:
        if element=='frac':
            indexnum=Input.index(element)
            if Input[indexnum+i]=='':
              Input.insert(indexnum+i,'by')
    return Input

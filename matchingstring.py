#to convert unrelated symbols to spaces
def latextolist(InputLatex):
    InputLatex = InputLatex.replace('\\{', '\\curlyopen')
    InputLatex = InputLatex.replace('\\}', '\\curlyclose')
    InputLatex = InputLatex.replace('{', ' ')
    InputLatex = InputLatex.replace('}', ' ')
    InputLatex = InputLatex.replace(',', ' ')
    Input = InputLatex.replace('\\', ' ')
    data=Input.split(' ')
    return data
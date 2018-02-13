def latextolist(InputLatex):
    InputLatex = InputLatex.replace('{', ' ')
    InputLatex = InputLatex.replace('}', ' ')
    InputLatex = InputLatex.replace('\\', ' ')
    return InputLatex
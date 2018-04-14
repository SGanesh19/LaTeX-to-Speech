import cx_Freeze
from cx_Freeze import *

setup(
    name="Latex2Speech",
    options = {'build_exe':{'packages':['gtts','pyglet','PyQt4']}},
    executables=[
        Executable(
            "prjui.py","Maiui.py","about.py","dict.py","geometry.py","getEquation.py",
            "gtrail.py","main.py","matchingstring.py","producelatex.py","readfile.py",
            "separete.py","speak.py",
        )
    ]

)

#ALL REQUIRED LIBRARIES ARE HERE=>
from setuptools import find_packages,setup
from typing import List

#CREATING CONSTANTS=>
HYPHEN_E_DOT = '-e .'

#FUNCTION TO READ ALL THE CONTENTS OF requirements.txt=>
def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #TO REMOVE EXTRA \n WHILE READING EACH LINE
        requirements = [req.replace('\n', ' ') for req in requirements]

        #CONDITION TO AVOID '-e .' IN requirements.txt
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

#CREATING A SETUP TO MAKE OUR PROJECT AS A PACKAGE SO ANYONE CAN USE IT=>
setup(
    name = 'mlproject',
    version= '0.0.1',
    author= 'Shubham Dubey',
    author_email= 'kumarshubhamdubey20@gmail.com',#OPTIONAL
    packages= find_packages(),#AUTOMATICALLY FINDS PROJECT MODELS LIKE, src/__init__
    install_requires = get_requirements("requirements.txt")
)

#NOTE:
'''
IMPORTANT: TO RUN THIS ENTIRE SETUP AND INSTALL ALL REQUIRED LIBRARIES 
JUST RUN A SIMPLE LINE OF STATEMENT IN THE TERMINAL AND ALL SET.

STATEMENT-> pip install -r requirements.txt
'''
from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requiremnts
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace('/n',' ') for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)

    return requirments

setup(
    name='mlproject',
    version='0.0.1',
    author='Sajad Ahmad mir',
    author_email='yours2312@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')

)
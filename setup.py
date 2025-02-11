from setuptools import find_packages,setup
from typing import List

HY_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    # This function  will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HY_E_DOT in requirements:
            requirements.remove(HY_E_DOT)
    
    return requirements

setup(
name='ML-E2E',
version='0.0.1',
author='Nishant',
author_email='nishantkadam1242@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
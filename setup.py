from setuptools import setup, find_packages
from typing import List

HYPHEN ='-e .'
def get_requirements(file_path:str)->List[str]:
    
    "this will return the list of requirements"
    
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace('\n','') for req in requirements]
        
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harsha',
    author_email='challapalliharsha123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

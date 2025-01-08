from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                #ignore the empty line and -e.
                if requirements and requirements !='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirement file not found") 

    return requirements_lst 
print(get_requirements())              

setup(
    name="Network Security",
    version="0.0.1",
    author="Nishant Kumbhar",
    author_email="nishantkumbhar812@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()

)

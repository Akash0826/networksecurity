'''
It is an essential part of packaging and distributing Python projects.
It provides metadata about the project and instructions on how to install it.
It is used by setuptools to define the package structure, dependencies, and other configurations.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Read the requirements from a file and return them as a list.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
            
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Akash M',
    author_email='akash.au19@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.10'
)
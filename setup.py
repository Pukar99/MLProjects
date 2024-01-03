from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='MLProjects',
    version='0.0.1',
    author='Pukar Sharma',
    author_email='sharma.pukar99@gmail.com',  
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # # Optional fields
    # long_description=open('README.md').read() if os.path.exists('README.md') else '',
    # url='https://github.com/Pukar99/MLProjects',  
)

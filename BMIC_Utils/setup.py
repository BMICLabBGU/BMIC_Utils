# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# python3 -m pip install --upgrade build
# python -m build

from typing import List
import re
from distutils.core import setup
from setuptools import find_packages
import os


def parseReqs(req_str:str)->List[str]:
    req_lst = req_str.split()
    req_ret = []
    
    p = re.compile("([0-9A-Z,a-z_\.]*)([><=]*)([0-9.]*)")
    for req in req_lst:
        m = p.match(req)
        new_str = "{:s}".format(m.group(1))
        if len(m.group(2))>0:
            new_str += " {:s} {:s}".format(m.group(2),m.group(3))
        
        req_ret.append(new_str)
        
        
    return req_ret
    


# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
long_description = 'DUDE'

try:
    with open(os.path.join(current_directory, 'requirements.txt'), encoding='utf-8') as f:
            reqs = f.read()
            reqs_lst = parseReqs(reqs)
except:
    reqs_lst = []
        
# Version
version = "0.1b0"
setup(
    # Project name: 
    name='BMIU',
    # Packages to include in the distribution: 
    packages=find_packages(','),
    # Project version number:
    version=version,
    # List a license for the project, eg. MIT License
    license='MIT License',
    # Short description of your library: 
    description='',
    # Long description of your library: 
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name: 
    author='BMIU Lab Group',
    # Your email address:
    author_email='bmiclabbgu@gmail.com',
    # Link to your github repository or website: 
    url='https://github.com/BMICLab',
    # Download Link from where the project can be downloaded from:
    download_url='https://github.com/BMICLab/BMIC_Utils.git',
    # List of keywords: 
    keywords=["Medical,Computer Vision, Deep Learning, MRI, CT"],
    # List project dependencies: 
    install_requires=reqs_lst,
    # https://pypi.org/classifiers/ 
    classifiers=[]
)
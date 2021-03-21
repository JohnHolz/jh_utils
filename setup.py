from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    ### simple info
     name='jh_utils', 
     version='0.0.1',
     author='João Holz',
     email = 'joaopaulo.paivaholz@gmail.com',
     description="Some simple functions to all projects",
     ## some descriptions
     long_description=long_description,
     long_description_content_type='text/markdown',
     ## github
     url='https://github.com/JohnHolz/jh_utils',
     packages=find_packages(),
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ],
     package_dir = {'': '.'},
     setup_requires=['wheel']
 )
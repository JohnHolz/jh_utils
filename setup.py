import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='jh_utils',  
     version='0.3',
     author='João Holz',
     email = 'joaopaulo.paivaholz@gmail.com',
     description="Some simple functions to all projects",
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/JohnHolz/jh_utils',
     packages=setuptools.find_packages(),
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ],
 )
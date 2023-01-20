from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name="Topsis_Ayush_102016100",
	version='1.2.2',
	author='Ayush Nagpure',
	author_email='anagpure_be20@thapar.edu',
	description='A python package to implement TOPSIS on a given dataset',
	long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
    python_requires='>=3.6',
	)
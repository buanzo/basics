# -*- coding: utf-8 -*-
from setuptools import setup
from os import path

# Imports content of requirements.txt into setuptools' install_requires
#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()


def get_version():
    with open('src/buanzobasics/buanzobasics.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


# Imports content of README.md into setuptools' long_description
#this_directory = path.abspath(path.dirname(__file__))
#with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()


description='A couple of useful functions like printerr, pprinterr, envOrDefault, etc'

setup(name='buanzobasics',
      version=get_version(),
      description=description,
      long_description=description,
      keywords='''python3,utility''',
      author='Arturo "Buanzo" Busleiman',
      author_email='buanzo@buanzo.com.ar',
      url='https://github.com/buanzo/basics',
      license='APL',
      zip_safe=False,
      python_requires='>=3.6',
      packages=['buanzobasics'],
      package_dir={'buanzobasics': 'src/buanzobasics'},
      classifiers=[
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'Operating System :: POSIX :: Linux',
         'Operating System :: POSIX :: Other',
         'Operating System :: POSIX',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3 :: Only',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: Implementation :: PyPy', ],)

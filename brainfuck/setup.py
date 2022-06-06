from setuptools import setup

setup(name='brainfuck',
        version='1.0',
        description='an interpreter for the brainfuck programming language',
        url='https://github.com/HorseScary/python-brainfuck',
        author='horse',
        author_email='horsescary@gmail.com',
        license='GPL3',
        packages=['brainfuck'],
        zip_safe=False,
        scripts=['bin/brainfuck'])

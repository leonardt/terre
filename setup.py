from setuptools import setup
import sys

setup(
    name='terre',
    version='0.1',
    description='A low-level system programming language embedded in Python',
    scripts=[],
    packages=[
        "terre",
    ],
    license='BSD License',
    url='https://github.com/leonardt/terre',
    author='Leonard Truong',
    author_email='lenny@cs.stanford.edu',
    python_requires='>=3.6'
)

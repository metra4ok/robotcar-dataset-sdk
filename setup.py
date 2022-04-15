import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'robotcar', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='robotcar',
      version='1.0',
      description='RobotCar Python SDK tools',
      author='Geoff Pascoe',
      author_email='gmp@robots.ox.ac.uk',
      packages=['robotcar'],
     )

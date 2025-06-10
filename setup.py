from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='pizzaprompt',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Carolina Amaya',
    author_email='camayag@poligran.edu.co',
    url='https://github.com/Carolina390/pizzaprompt',
    packages=find_packages(exclude=('tests'))
)
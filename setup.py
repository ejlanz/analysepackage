from setuptools import setup, find_packages

setup(
    name='analysepackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ejlanz/analysepackage.git',
    author='Ernest John Lanz',
    author_email='ejlanz.za@gmail.com'
)

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pyDecision',
    version='2.8.3',
    license='GNU',
    author='Valdecy Pereira',
    author_email='valdecy.pereira@gmail.com',
    url='https://github.com/Valdecy/pyDecisions',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'scikit-learn'
    ],
    description='A MCDA Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
)

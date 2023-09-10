from setuptools import setup, find_packages

setup(
    name='jumpsuit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'statsmodels',
        'matplotlib'
    ],
)

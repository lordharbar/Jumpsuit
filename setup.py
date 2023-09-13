from setuptools import setup, find_packages

setup(
    name='jumpsuit',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'statsmodels',
        'matplotlib',
        'xgboost',
        'scikit-learn'
    ],
)

import os, sys
from setuptools import setup, find_packages

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except:
        return ''

DESC = " ".join(__import__('alphafilter').__doc__.splitlines()).strip()

setup(
    name = "django-alphafilter",
    version = __import__('alphafilter').get_version().replace(' ', '-'),
    url = 'http://github.com/coordt/django-alphabetfilter',
    author = 'Corey Oordt',
    author_email = 'coreyoordt@gmail.com',
    description = DESC,
    long_description = read_file('README.rst'),
    packages = find_packages(),
    license = 'Apache 2.0',
    include_package_data = True,
    install_requires=read_file('requirements.txt'),
    zip_safe = False,
    classifiers = [
    ],
)

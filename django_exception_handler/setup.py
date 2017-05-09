import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-exception-handler',
    version='0.1',
    packages=['django_exception_handler'],
    description='A library to handle possible exceptions',
    long_description=README,
    author='devRahul',
    author_email='rahul1991.c@gmail.com',
    url='https://github.com/nimeshkverma/Imp/django_exception_handler/',
    license='Marvels',
    install_requires=[
        'Django>=1.6,<1.7',
    ]
)

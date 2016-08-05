import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='django-floppyforms-bootstrap3',
    version='0.0.1',
    packages=['floppyforms_bootstrap3',],
    description='A Plugin for Django Floppy Forms that provides Bootstrap 3 based form templates.',
    long_description=(read('README.md')),
    url='https://github.com/grundleborg/django-floppyforms-bootstrap3',
    license='MIT',
    author='George Goldberg',
    author_email='george@grundleborg.com',
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[ "django-floppyforms", ],
)

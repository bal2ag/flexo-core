"""
Flexo-Core
-------

Flexo makes service and API development in Python fun and easy.
"""
import ast, re

from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('flexo/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='Flexo-Core',
    version=version,
    url='http://github.com/bal2ag/flexo-core/',
    license='BSD',
    author='Alex Landau',
    author_email='toozlyllc@gmail.com',
    description='Core library for the Flexo service framework',
    long_description=__doc__,
    packages=['flexo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests>=2.11.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
    

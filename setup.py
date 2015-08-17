import os
import re

from setuptools import setup, find_packages


MODULE_NAME = 'juju_scaleway'

DEPENDENCIES = [
    'PyYAML',
    'requests',
    'ndg-httpsclient >=0.3.3',
]

TEST_DEPENDENCIES = [
    'mock'
]

EXTRA_DEPENDENCIES = {
    'dev': ['PyYAML', 'requests', 'nose', 'mock']
}


def get_version():
    """ Reads package version number from package's __init__.py. """
    with open(os.path.join(
        os.path.dirname(__file__), MODULE_NAME, '__init__.py'
    )) as init:
        for line in init.readlines():
            res = re.match(r'^__version__ = [\'"](.*)[\'"]$', line)
            if res:
                return res.group(1)

def get_long_description():
    """ Read description from README and CHANGES. """
    with open(
        os.path.join(os.path.dirname(__file__), 'README.md')
    ) as readme, open(
        os.path.join(os.path.dirname(__file__), 'CHANGES.md')
    ) as changes:
        return readme.read() + '\n' + changes.read()

setup(
    name='juju-scaleway',
    version=get_version(),
    author='Scaleway',
    author_email='opensource@scaleway.com',
    description='Scaleway integration with juju',
    url='https://pypi.python.org/pypi/juju-scaleway',
    license='BSD',
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    tests_require=DEPENDENCIES + TEST_DEPENDENCIES,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
    ],
    entry_points={
        'console_scripts': [
            'juju-scaleway = juju_scaleway.cli:main'
        ]
    },
    extras_require=EXTRA_DEPENDENCIES
)

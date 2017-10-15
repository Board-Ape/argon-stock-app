try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Argon',
    'author': 'Bryan Deloeste',
    'url': 'https://gitlab.com/bdeloeste/argon',
    'download_url': 'git@gitlab.com:bdeloeste/argon.git',
    'author_email': 'bryandeloeste@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['argon'],
    'scripts': [],
    'name': 'argon'
}

setup(**config)

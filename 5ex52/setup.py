try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'My Project',
'author': 'Daniella Stalingovskis',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'dstal004@fiu.edu',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex52'],
'scripts': [],
'name': 'ex52'
}

setup(**config)

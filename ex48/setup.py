try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description'      : 'My Project',
    'author'           : 'Josh English',
    'url'              : 'www.joshenglish.com',
    'download_url'     : 'www.joshenglish.com',
    'author_email'     : 'My Email',
    'version'          : '0.1',
    'install_requires' : ['nose'],
    'packages'         : ['ex48'],
    'scripts'          : [],
    'name'             : 'projectname'
}


setup(**config)
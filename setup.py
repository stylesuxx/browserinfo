from distutils.core import setup

from browserinfo import __version__

setup(
    name='browserinfo',
    version=__version__,
    description='API wrapper for browser-info.net',
    long_description=open('README.md').read(),
    author='Chris Landa',
    author_email='stylesuxx@gmail.com',
    url='https://github.com/stylesuxx/browserinfo',
    license='MIT',
    packages=['browserinfo'])

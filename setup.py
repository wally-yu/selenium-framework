from setuptools import setup, find_packages
import codecs
import re, os

with open('README.md') as readme_file:
    long_description = readme_file.read()


def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


file_text = read(fpath('selenium_framework/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    name='pyselenium_framework',
    version=grep('__version__'),
    packages=find_packages(),
    author=u'Wally Yu',
    install_requires=['selenium==3.141.0'],
    url='https://github.com/wally-yu/selenium-framework',
    include_package_data=True,
    license='MIT License',
    description='A Python Selenium Framework Which Makes Code More Easy to Maintain and Read',
    long_description=long_description,
    long_description_content_type='text/markdown',
      )

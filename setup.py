from setuptools import setup, find_packages

setup(name='emuSync',
      version='1.0',
      description='iSYSTEM emuSync',
      author='iSYSTEM',
      author_email='support@isystem.com',
      url='https://www.isystem.com/',
      install_requires=[
          "isystem.connect",
          "pyyaml"
      ]
      )

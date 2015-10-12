# ----------------------------------------------------
# setup.py
# Author: Chris Apple
# Last Edited: 10/12/15
# Description: setup.py for installing custom packages
# Run with command: python setup.py develop
# ---------------------------------------------------- 


from distutils.core import setup
import setuptools

setup(name='Lido',
      version='1.0',
      packages=['src/content', 'src/hardware']
      )

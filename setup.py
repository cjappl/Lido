# ----------------------------------------------------
# setup.py
# Author: Chris Apple
# Last Edited: 10/12/15
# Description: setup.py for installing custom packages
# Run with command: python setup.py develop
# ----------------------------------------------------

PROJECT_NAME = "Lido Project"

from distutils.core import setup
import setuptools

setup(name=PROJECT_NAME,
      version="1.0",
      description="Lido Project for KW, CA",
      package_dir={'': 'src'},
      packages=["content", "hardware"],

      zip_safe=False,

      install_requires=[
          "numpy",
          "pydub>0.14.0",
          "pytest>2.7"
      ],

      author="Chris Apple, Kaya Woodall",
      author_email="christopher.j.apple@gmail.com, kwoodall@hmc.edu"
      )

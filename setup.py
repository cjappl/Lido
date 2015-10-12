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

setup(name="Lido",
      version="1.0",
      description="Lido Project for KW, CA",
      packages=["src/content", "src/hardware"],

      zip_safe=False,

      install_requires=[
          "pydub>0.14.0"
      ],

      author="Chris Apple, Kaya Woodall",
      author_email="christopher.j.apple@gmail.com, kwoodall@hmc.edu"
      )

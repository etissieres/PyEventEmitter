#!/usr/bin/env python

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

classifiers = [
    "Programming Language :: Python",
    "Development Status :: 4 - Beta",
    "License :: OSI Approved",
    "Natural Language :: French",
    "Operating System :: OS Independent",
    "Topic :: Utilities",
]

setup(name='PyEventEmitter',
      version='0.1.3',
      description='Simple python events library',
      long_description=long_description,
      author='Etienne Tissieres',
      author_email='etienne.tissieres@gmail.com',
      url='https://github.com/etissieres/PyEventEmitter',
      packages=['py_event_emitter'],
      license='MIT',
      classifiers=classifiers)

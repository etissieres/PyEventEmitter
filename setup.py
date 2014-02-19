#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='PyEventEmitter',
      version='1.1',
      description='Simple python events library',
      long_description=long_description,
      author='Etienne Tissieres',
      author_email='etienne.tissieres@gmail.com',
      url='https://github.com/etissieres/PyEventEmitter',
      packages=['py_event_emitter'],
      license='MIT')

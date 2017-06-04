#!/usr/bin/env python

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

classifiers = [
    'Programming Language :: Python :: 3',
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved',
    'Intended Audience :: Developers',
    'Natural Language :: French',
    'Operating System :: OS Independent',
    'Topic :: Utilities',
]

setup(name='PyEventEmitter',
      version='1.0.4',
      description='Simple python events library',
      long_description=long_description,
      author='Etienne Tissieres',
      author_email='etienne.tissieres@gmail.com',
      url='https://github.com/etissieres/PyEventEmitter',
      packages=['event_emitter'],
      license='MIT',
      classifiers=classifiers)

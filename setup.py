#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
  name='wagtail-cloudfront-invalidate',
  version='1.0.1',
  description="A wagtail hook to invalidate AWS's CloudFront cache when a page is updated",
  long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
  author='Ryan Bagwell',
  author_email='ryan@ryanbagwell.com',
  url='https://github.com/ryanbagwell/wagtail-cloudfront-invalidate/',
  packages=find_packages(),
  classifiers=[
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
  ],
  install_requires=[
    'django>=1.11.0',
    'boto3>=1.9.112',
    'wagtail>=2.0.0',
  ]
)
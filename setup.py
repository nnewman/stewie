#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt',
                                  session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='stewie',
      version='0.9.1',
      description='A minimal extensible bot for Mattermost',
      author='Neil Newman',
      url='https://github.com/nnewman/stewie',
      packages=['stewie'],
      package_data={
            'stewie': ['stewie.md']
      },
      include_package_data=True,
      install_requires=reqs,
      )

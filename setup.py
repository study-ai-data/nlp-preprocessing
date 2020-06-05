# !/usr/bin/env python

from setuptools import setup, find_packages
import preprocess


def install():
    setup(name=preprocess.__name__,
          description=preprocess.__description__,
          version=preprocess.__version__,
          author=['Kyeongnam Kim'],
          author_email=['devokkn@gmail.com'],
          url=preprocess.__url__,
          download_url=preprocess.__download_url__,
          install_requires=preprocess.__install_requires__,
          license=preprocess.__license__,
          long_description=open('./README.md', 'r', encoding='utf-8').read(),
          packages=find_packages(),
          classifiers=[
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.2',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'Programming Language :: Python :: 3.9',
          ]
          )


if __name__ == "__main__":
    install()

#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import versioneer

extras_require = {
  'array': ['numpy', 'toolz >= 0.7.2'],
  'bag': ['cloudpickle >= 0.2.1', 'toolz >= 0.7.2', 'partd >= 0.3.5'],
  'dataframe': ['numpy', 'pandas >= 0.18.0', 'toolz >= 0.7.2',
                'partd >= 0.3.5', 'cloudpickle >= 0.2.1'],
  'distributed': ['distributed >= 1.10', 's3fs'],
  'imperative': ['toolz >= 0.7.2'],
}
extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

packages = ['dask', 'dask.array', 'dask.bag', 'dask.store', 'dask.bytes',
            'dask.dataframe', 'dask.dataframe.io', 'dask.dataframe.tseries',
            'dask.diagnostics']

tests = [p + '.tests' for p in packages]


setup(name='dask',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Minimal task scheduling abstraction',
      url='http://github.com/dask/dask/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='task-scheduling parallelism',
      packages=packages + tests,
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      install_requires=extras_require['dataframe'],
      extras_require=extras_require,
      zip_safe=False)

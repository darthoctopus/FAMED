from setuptools import setup, find_packages
# from numpy.distutils.core import build_ext, build_src, Extension
import os

'''
with open('expres/VERSION', 'r') as f:
    version = f.readline()

ext_modules = [
    Extension(name='rv',
              sources=['expres/rv/ccf/rv.f90',
                       'expres/rv/ccf/hermiteccflib.f90',
                       'expres/rv/ccf/rv.pyf']
              )
]
cmdclass = {'build_ext': build_ext.build_ext, 'build_src': build_src.build_src}
'''

if __name__ == '__main__':
    setup(name='famed',
          version="0.0.1",
          author='Enrico Corsaro, Jean McKeever, James Kuslewicz',
          author_email='enrico.corsaro@inaf.it',
          description='Python wrapper for DIAMONDS tooling',
          license='MIT',
          url='https://github.com/EnricoCorsaro/FAMED',
          packages=find_packages(),
          # cmdclass=cmdclass,
          # ext_modules=ext_modules,
          install_requires=['numpy', 'scipy', 'statistics', 'matplotlib']
          )

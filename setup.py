from setuptools import setup

setup(
    name='hgs_tool',
    version='1.0',
    description = 'A Python package for working with HGS.',
    author = 'Fan Yang',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Microsoft :: Windows',
        ],
    keywords = 'hydrogeosphere',
    packages = ['convert_tecplot', 'write_include'],
    install_requires = ['numpy', 'pandas'],
      )
import os
from setuptools import setup, find_packages


setup(
    name='libkeepass',
    version='0.0.3',
    description="Python module to read KeePass 1.x/KeePassX (v3) and KeePass "
                "2.x (v4) files",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
    author='Florian Demmer',
    author_email='fdemmer@gmail.com',
    packages=find_packages(),
    keywords="libkeepass",
    url="https://github.com/fdemmer/libkeepass",
    install_requires=[
        'lxml==3.2.1',
        'nose==1.3.0',
        'pycrypto==2.6',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
)

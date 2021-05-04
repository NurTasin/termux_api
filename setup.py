from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "termux_api",
    version = "1.0.0",
    author = "Nur Mahmud Ul Alam Tasin",
    author_email = "nmuatasin2005@gmail.com",
    description = ("A Binding for Termux:API written in python with feature rich functionality."),
    license = "MIT",
    keywords = "termux bindings api apis",
    url = "https://github.com/NurTasin/termux_api",
    packages=find_packages(),
    long_description=read('README.md')
)
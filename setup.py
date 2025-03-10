from setuptools import setup
from setuptools import find_packages

with open("requirements.txt", "r") as file:
    lines = file.readlines()
reqs = [each.strip() for each in lines]

setup(name="cookies", packages=find_packages(), install_requires=reqs)

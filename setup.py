import os

from setuptools import setup, find_packages


working_dir = os.getcwd()

with open(f"{working_dir}/README.md", "r") as readme:
    README = readme.read()

with open(f'{working_dir}/VERSION', 'r') as version:
    VERSION = version.readline()

with open(f'{working_dir}/requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='webpcon',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/Techi-Freki/webp_converter',
    license='MIT',
    author='Techi-Freki',
    description='Converts a webp into either a JPG or PNG',
    long_description=README,
    long_description_content_type='markdown/text',
    install_requires=REQUIREMENTS
)

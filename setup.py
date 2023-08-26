from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='discord.py',
    author='smugay',
    description='Python wrapper for interacting txts',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/txts-team/txts.py/',
    version="1.0",
    packages=find_packages(),
    install_requires=requirements,
classifiers=[
        "Programming Language :: Python 3",
        "License :: MIT"
    ],
    python_requires='>=3.3'
)
from setuptools import setup, find_packages

setup(
    name="openWeatherMap-SDK",
    version="1.0.0",
    install_requires=[
        requests,
        ],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Dan7706",                   
    author_email="Author's email",          
    url="https://github.com/Dan7706/SDK",     
    )

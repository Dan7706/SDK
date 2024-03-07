Upload and Integration of a Python SDK:
1. Prepare your SDK by creating a project structure:
    My_SDK/
    |__MySDK/
    |  |-__init__.py
    |  |-main.py
    |
    |_setup.py
    |_README.md
    
    main.py file contains the SDK driver code, __init__.py is neccessary to make it as a package,
    setup.py file contains all the setup information mentioned below and README file is the description of your project.


2.Install neccessary packages:
    pip install setuptools wheel twine

3.Building an SDK:
    python setup.py sdist bdist_wheel
    After this command you will see two new folders in the same directory:
        build/
        dist/

4.Local testing(you can run this command to local testing):
    pip install dist/My_SDK_1.0.0-py3-none-any-whl

5.Uploading to PYPI:
    twine upload dist/*
    (before uploading you have to register an account in pypi.org as after the upload command
     your creditentials needed)

6.Test Repository Uploading:
    You are also able to upload your code to PYPI test repository:
    twine upload --repository testpypi dist/*

    And install from test repository with pip:
    pip install --index-url https://test.pypi.org/simple/your_sdk-your-username


AT LEAST THE setup.py FILE EXAMPLE:

#setup.py

from setuptools import setup, find_packages

setup(
    name="your_SDK_name", #your directory name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        #List of dependencies if ther are any
        ],
    description="Your SDK description",
    long_description=open('README.me", "r").read(), #you have to write inside README
    long_description_content_type="text/markdown",
    author="Author's Name",                        #non mandatory
    author_email="Author's email",                 #non mandatory
    url="https://github.com/yourusername/sdk_repo  #non mandatory
    
    )

P.S "This is a brief introduction to SDKs. Of course there are more details and nuances 
    to build a specific SDK. You can visit 

    docs.python.org/2/distutils/setupscript.html 
    or
    packaging.python.org/en/latest/tutorials/packaging-projects
    
    website for more details."


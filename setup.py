from distutils.core import setup
from os import read

def get_readme():
    with open("README.md","r") as file:
        readme = file.read()
    return readme

def get_requirements():
    with open("requirements.txt","r") as req:
        requirements = req.read()
    return requirements

setup(name="imagedownloader"
    ,version="1.0,"
    ,description="A image downloader library tool created by love."
    ,author="Md Masud karim"
    ,author_email="msmasud578@gmail.com"
    ,long_description=get_readme()
    ,long_description_content_type="text/markdown"
    ,packages=["src"]
    ,include_package_data=True
    ,install_requires= get_requirements()
    )
from setuptools import find_packages
from setuptools import setup

setup(
    name="github_api_wrapper",
    version="0.1",
    author="Mariam Jamal",
    author_email="mjamal@folio3.com",
    description="Package to provide utility tools for Github Pull Requests",
    long_description="Package to provide find pull requests for Github repos"
                     "with commit and file filters",
    long_description_content_type="text/markdown",
    url="https://github.com/oakbani/f3Github",
    packages=find_packages(
      exclude=['tests']
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

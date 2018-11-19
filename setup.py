from setuptools import find_packages
from setuptools import setup

setup(
    name="f3Github",
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
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='f3Github.tests',
)

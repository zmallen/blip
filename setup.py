import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="blip",
    version="0.1.0",
    description="Turn a target string into a list of bit flipped strings",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zmallen/blip",
    author="techy",
    packages=find_packages(include=['blip']),
    author_email="zma4580@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "blip=blip.blip:main",
        ]
    },
)

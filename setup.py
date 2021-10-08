import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="betting",
    version="0.0.2",
    description="Utility library for converting between betting odds",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/decisionmechanics/betting",
    author="Andrew Tait",
    author_email="dev@decisionmechanics.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=("tests",)),
)

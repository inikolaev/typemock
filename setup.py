import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typemock",
    version="0.0.1",
    author="Laurence Willmore",
    description="Type safe mocking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lgwillmore/type-mock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
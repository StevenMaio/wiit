import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="wiit",
	version="0.1",
	author="Steven Maio",
	author_email="stevenmaio.321@gmail.com",
	description="A tool for managing pdf files",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/StevenMaio/wiit",
	packages=setuptools.find_packages(),
	classifiers= [
		"Programming Language :: Python :: 3",
	],
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rafeequewoods/__init__.py
from rafeequewoods import __version__ as version

setup(
	name="rafeequewoods",
	version=version,
	description="wood industry",
	author="wahni green technologies",
	author_email="safvanph41@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

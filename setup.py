from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cfdi/__init__.py
from cfdi import __version__ as version

setup(
	name="cfdi",
	version=version,
	description="Facturacion Electronica MX",
	author="gdelriou",
	author_email="gilberto_garcia_del_rio@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

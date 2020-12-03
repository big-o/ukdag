from setuptools import find_packages, setup

setup(
    name="ukdag",
    version="0.0.1",
    description="Directed acyclic graph of UK administrative boundaries.",
    url="http://github.com/big-o/ukdag",
    author="big-o",
    author_email="big-o@users.noreply.github.com",
    license="GPLv3",
    packages=find_packages(exclude="test"),
)

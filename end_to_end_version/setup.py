from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as requirements_file:
        requirements = requirements_file.readlines()
        requirements = [req.replace("\n","") for req in requirements if req!="-e ."]
    return requirements

setup(
    name="End to end project",
    version="0.1.0",
    author="Daniel Izaguirre",
    author_email="izaguirredaniel9712@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
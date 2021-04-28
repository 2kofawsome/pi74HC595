from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pi74HC595",
    author="Sam Gunter",
    author_email="samgunter12@gmail.com",
    version="1.2.3",
    license="MIT",
    keywords="Raspberry Pi GPIO 74HC595",
    url="https://github.com/2kofawsome/pi74HC595",
    description="Use the 74HC595 Shift Register with a Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
    ],
)

from setuptools import find_packages, setup
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version = "2.1.1"

setup(
    name="pyairports",
    version=version,
    description="Airport and other locations database",
    long_description=long_description,
    url="https://github.com/ozeliger/pyairports",
    author="Jason Dsouza",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="Airports",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # Requirements go here
    install_requires=[],
    # Requrements for specific build cycles go here
    # { 'build': [requirements,for,build] }
    extras_require={},

    # For data files within your package
    # { package_name: [filenames, in, the, package] }
    package_data={
        'pyairports': ['data/airport_list.json', 'data/other_list.json']
    },

    # For data files outside your package
    # [ ( directory, [filenames, in, the, directory] }
    data_files=[],

    # Define entry points to your program
    # "command=package:function"
    entry_points={
        "console_scripts": [
            "pyairports=pyairports.airports:main"
        ],
    },
    test_suite='nose.collector',
    tests_require=['nosexcover'],
)

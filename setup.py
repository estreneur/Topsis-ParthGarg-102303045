from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-ParthGarg-102303045",
    version="1.0.2",
    author="Parth Garg",
    author_email="pgarg1_be23@thapar.edu",
    description="A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prathamgarg/Topsis-Pratham-102303052",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",
        ],
    },
)

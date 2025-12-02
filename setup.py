"""
Setup script for COMALLS + Latin Square Clinical Trial Toolkit
"""

from setuptools import setup, find_packages
import pathlib

# Read README for PyPI description
ROOT = pathlib.Path(__file__).parent
README = (ROOT / "README.md").read_text(encoding="utf-8")

setup(
    name="comalls-latin-square",
    version="1.0.0",
    author="Md Tariqul Islam",
    author_email="tariqul@scired.com",
    description=(
        "Unified toolkit for Latin Square clinical trial simulation and "
        "COMALLS context-controlled machine learning using Latin Square scheduling."
    ),
    long_description=README,
    long_description_content_type="text/markdown",

    url="https://github.com/mtariqi/latin-square-clinical-trial",
    project_urls={
        "Bug Tracker": "https://github.com/mtariqi/latin-square-clinical-trial/issues",
        "Documentation": "https://mtariqi.github.io/latin-square-clinical-trial/",
        "Source Code": "https://github.com/mtariqi/latin-square-clinical-trial",
        "Sphinx Docs": "https://mtariqi.github.io/latin-square-clinical-trial/",
        "COMALLS Paper": "https://github.com/mtariqi/latin-square-clinical-trial/tree/main/paper",
    },

    packages=find_packages(exclude=("tests*", "paper*", "docs*", "examples*")),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",

        # Python versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.7",

    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.1.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
        "scipy>=1.5.0",
    ],

    extras_require={
        "dev": [
            "pytest>=6.0",

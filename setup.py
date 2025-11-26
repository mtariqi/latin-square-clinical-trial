"""
Setup script for Latin Square Clinical Trial Analyzer.
"""

from setuptools import setup, find_packages
import pathlib

# Read the contents of README file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="latin-square-analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A toolkit for designing and analyzing Latin Square crossover clinical trials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/latin-square-clinical-trial",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/latin-square-clinical-trial/issues",
        "Documentation": "https://github.com/yourusername/latin-square-clinical-trial/blob/main/README.md",
        "Source Code": "https://github.com/yourusername/latin-square-clinical-trial",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
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
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
            "pylint>=2.8",
            "jupyter>=1.0",
            "notebook>=6.4",
        ],
    },
    keywords=[
        "latin-square",
        "clinical-trials",
        "crossover-design",
        "biostatistics",
        "experimental-design",
        "anova",
        "health-science",
    ],
    include_package_data=True,
    zip_safe=False,
)

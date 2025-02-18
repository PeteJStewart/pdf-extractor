from setuptools import setup, find_packages

setup(
    name="pdf-extractor",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "PyMuPDF>=1.23.0",
        "pytesseract>=0.3.10",
        "Pillow>=10.0.0",
    ],
) 
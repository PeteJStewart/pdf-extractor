import importlib.util
from pytesseract import image_to_string as _image_to_string

def is_package_installed(package_name: str) -> bool:
    """Check if a package is installed using importlib"""
    return importlib.util.find_spec(package_name) is not None

def image_to_string(image) -> str:
    """Wrapper around pytesseract's image_to_string that uses modern imports"""
    return _image_to_string(image) 
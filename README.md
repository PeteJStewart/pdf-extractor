# PDF Text Extraction Tool

This repository contains a Python script that extracts text from PDF files. It supports both text-based and image-based PDFs (using OCR). The extracted text is saved along with metadata (such as the source PDF file name and page numbers), and a log file is generated to track successfully processed and failed files.

## Features

- **Batch Processing:** Extract text from all PDFs in a specified directory.
- **OCR Support:** Automatically performs OCR on pages that do not contain extractable text.
- **Metadata Logging:** Saves extracted text with page markers and logs which PDFs were processed successfully or failed.
- **Smart Processing:** Tracks processed files to avoid reprocessing the same PDFs multiple times.
- **Testing Mode:** Optionally limit the number of PDFs to process (ideal for testing).

## Requirements

- **Python:** 3.7+
- **Python Packages:**
  - [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (for PDF text extraction)
  - [pytesseract](https://pypi.org/project/pytesseract/) (for OCR)
  - [Pillow](https://python-pillow.org/) (for image processing)

**System Dependency:**
- [Tesseract OCR Engine](https://github.com/tesseract-ocr/tesseract)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PeteJStewart/pdf-extractor.git
cd pdf-extractor
```

### 2. Set Up a Virtual Environment (Recommended)

#### On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Dependencies

Make sure you have [pip](https://pip.pypa.io/) installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

#### Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install tesseract-ocr
```

For other Linux distributions, use your package manager (e.g., `yum`, `dnf`).

#### macOS:

Install Tesseract using [Homebrew](https://brew.sh/):

```bash
brew install tesseract
```

#### Windows:

Download the installer from the [Tesseract at UB Mannheim page](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.  
> **Note:** After installing, ensure that the Tesseract executable is added to your system's PATH so that `pytesseract` can access it.

## Usage

The script can be run from the command line with the following arguments:

- `--from-dir`: The source directory containing PDFs to process
- `--to-dir`: The output directory where the extracted text files and log will be saved
- `--limit`: (Optional) The number of PDFs to process (useful for testing)

### Example Command

#### Linux/macOS:

```bash
python -m pdf_extractor.extract_pdfs --from-dir "/path/to/pdf_directory" --to-dir "/path/to/output_directory" --limit 5
```

#### Windows:

```bash
python -m pdf_extractor.extract_pdfs --from-dir "C:\path\to\pdf_directory" --to-dir "C:\path\to\output_directory" --limit 5
```

This command processes up to 5 PDF files from the specified source directory, extracts their text (using OCR when necessary), and writes the output as text files into the target directory. A log file (`extraction_log.txt`) is also created to list the successful and failed extractions.

## Testing

To run the tests:

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Run the tests:
```bash
pytest
```

The tests verify that:
- Files are properly processed on first run
- Previously processed files are skipped on subsequent runs
- The log file correctly tracks processed files

## Project Structure
```go
    pdf-extractor/
    ├── pdf_extractor/          # Main package directory
    │   ├── __init__.py
    │   ├── extract_pdfs.py     # Core extraction logic
    │   └── tesseract_wrapper.py # OCR wrapper
    ├── tests/                  # Test directory
    │   ├── __init__.py
    │   └── test_extract_pdfs.py
    ├── setup.py               # Package configuration
    ├── requirements.txt       # Production dependencies
    ├── requirements-dev.txt   # Development dependencies
    └── pytest.ini            # Test configuration
```

## Additional Information

- **Error Handling:** Failed PDFs are logged in the `extraction_log.txt` file
- **Progress Tracking:** The log file keeps track of processed files to avoid redundant processing
- **Contributions:** Feel free to open issues or submit pull requests
- **License:** This project is licensed under the MIT License

## Troubleshooting

- **Tesseract Not Found:** Ensure Tesseract is installed and in your system's PATH
- **Import Errors:** Make sure you're in your virtual environment and have installed all dependencies
- **Processing Errors:** Check the extraction log for details about failed files

Happy extracting!

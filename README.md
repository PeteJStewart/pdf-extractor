# PDF Text Extraction Tool

This repository contains a Python script that extracts text from PDF files. It supports both text-based and image-based PDFs (using OCR). The extracted text is saved along with metadata (such as the source PDF file name and page numbers), and a log file is generated to track successfully processed and failed files.

## Features

- **Batch Processing:** Extract text from all PDFs in a specified directory.
- **OCR Support:** Automatically performs OCR on pages that do not contain extractable text.
- **Metadata Logging:** Saves extracted text with page markers and logs which PDFs were processed successfully or failed.
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

The script `extract_pdfs.py` takes the following command-line arguments:

- `--from-dir`: The source directory containing PDFs to process.
- `--to-dir`: The output directory where the extracted text files and log will be saved.
- `--limit`: *(Optional)* The number of PDFs to process (useful for testing).

### Example Command

#### Linux/macOS:

```bash
python extract_pdfs.py --from-dir "/path/to/pdf_directory" --to-dir "/path/to/output_directory" --limit 5
```

#### Windows:

```bash
python extract_pdfs.py --from-dir "C:\path\to\pdf_directory" --to-dir "C:\path\to\output_directory" --limit 5
```

This command processes up to 5 PDF files from the specified source directory, extracts their text (using OCR when necessary), and writes the output as text files into the target directory. A log file (`extraction_log.txt`) is also created to list the successful and failed extractions.

## Additional Information

- **Error Handling:** If a PDF fails to process, it will be logged in the `extraction_log.txt` file.
- **Modularity:** You can modify the extraction function to suit your needs (e.g., change text segmentation, add more metadata).
- **Contributions:** Feel free to open issues or submit pull requests if you have suggestions or improvements.
- **License:** This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Troubleshooting

- **Tesseract Not Found:** Ensure that Tesseract is installed and its executable is in your system's PATH.
- **Dependency Issues:** Double-check that all Python dependencies are installed using `pip install -r requirements.txt`.

Happy extracting!

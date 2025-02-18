#!/usr/bin/env python3
import os
import argparse
import fitz  # PyMuPDF
from PIL import Image
import io
from .tesseract_wrapper import image_to_string

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    Uses direct extraction; if a page has no text, performs OCR.
    Returns a string with all pages' text including page markers.
    """
    doc = fitz.open(pdf_path)
    extracted_text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        # Attempt to extract text normally
        text = page.get_text().strip()
        
        if not text:
            # Convert page to image for OCR if no text is found
            pix = page.get_pixmap()
            img_bytes = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_bytes))
            text = image_to_string(image)  # Using our wrapper
        
        # Include page number as metadata
        extracted_text.append(f"--- Page {page_num + 1} ---\n{text}")
    
    return "\n\n".join(extracted_text)

def load_processed_files(log_file):
    """Load list of successfully processed files from log file."""
    if not os.path.exists(log_file):
        return set()
    
    processed_files = set()
    try:
        with open(log_file, 'r', encoding='utf-8') as log:
            in_success_section = False
            for line in log:
                if line.strip() == "Successful Files:":
                    in_success_section = True
                elif line.strip() == "Failed Files:":
                    in_success_section = False
                elif in_success_section and line.strip():
                    processed_files.add(line.strip())
    except Exception as e:
        print(f"Warning: Could not load log file: {e}")
    return processed_files

def main(from_dir, to_dir, limit):
    # Check source directory exists
    if not os.path.isdir(from_dir):
        print(f"Error: The source directory '{from_dir}' does not exist.")
        return
    
    # Create the output directory if it doesn't exist
    os.makedirs(to_dir, exist_ok=True)
    
    # Load already processed files
    log_file = os.path.join(to_dir, "extraction_log.txt")
    processed_files = load_processed_files(log_file)

    # Gather all PDF files from the source directory
    pdf_files = [f for f in os.listdir(from_dir) 
                 if f.lower().endswith('.pdf') and f not in processed_files]
    
    # Apply the limit if provided
    if limit is not None:
        pdf_files = pdf_files[:limit]
    
    success_list = []
    failed_list = []

    for pdf_file in pdf_files:
        pdf_path = os.path.join(from_dir, pdf_file)
        print(f"Processing: {pdf_file}")
        try:
            text = extract_text_from_pdf(pdf_path)
            # Write the extracted text to a .txt file in the output directory
            base_name = os.path.splitext(pdf_file)[0]
            output_file = os.path.join(to_dir, f"{base_name}.txt")
            with open(output_file, 'w', encoding='utf-8') as f_out:
                f_out.write(text)
            success_list.append(pdf_file)
        except Exception as e:
            print(f"Failed to process '{pdf_file}': {e}")
            failed_list.append(pdf_file)
    
    # Write a log file to track successes and failures
    if not os.path.exists(log_file):
        # Create new log file if it doesn't exist
        with open(log_file, 'w', encoding='utf-8') as log:
            log.write("Extraction Log\n")
            log.write("====================\n")
            log.write("Successful Files:\n")
            log.write("\nFailed Files:\n")
    
    # Append new successes and failures
    with open(log_file, 'r+', encoding='utf-8') as log:
        content = log.readlines()
        # Find the "Successful Files:" section
        for i, line in enumerate(content):
            if line.strip() == "Successful Files:":
                # Insert new successes after this line
                for file in success_list:
                    content.insert(i + 1, f"{file}\n")
                break
        
        # Find the "Failed Files:" section
        for i, line in enumerate(content):
            if line.strip() == "Failed Files:":
                # Insert new failures after this line
                for file in failed_list:
                    content.insert(i + 1, f"{file}\n")
                break
        
        # Write the updated content back to the file
        log.seek(0)
        log.writelines(content)
    
    print("\nExtraction complete.")
    print("Successful PDFs:", success_list)
    print("Failed PDFs:", failed_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract text from all PDF files in a directory with optional OCR for image-based pages."
    )
    parser.add_argument(
        "--from-dir", type=str, required=True,
        help="Path to the directory containing PDFs to process."
    )
    parser.add_argument(
        "--to-dir", type=str, required=True,
        help="Path to the directory where extracted text files and log will be saved."
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Limit the number of PDFs to process (for testing purposes)."
    )
    args = parser.parse_args()
    
    main(args.from_dir, args.to_dir, args.limit)

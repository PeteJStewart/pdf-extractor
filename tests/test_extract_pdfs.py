import os
import tempfile
import pytest
from pdf_extractor.extract_pdfs import main, extract_text_from_pdf, load_processed_files

@pytest.fixture
def temp_dirs():
    """Create temporary directories for testing"""
    with tempfile.TemporaryDirectory() as from_dir:
        with tempfile.TemporaryDirectory() as to_dir:
            # Create a mock PDF file (we'll just use an empty file for testing)
            pdf_path = os.path.join(from_dir, "test1.pdf")
            with open(pdf_path, "w") as f:
                f.write("dummy pdf")
            
            pdf_path2 = os.path.join(from_dir, "test2.pdf")
            with open(pdf_path2, "w") as f:
                f.write("dummy pdf 2")
                
            yield from_dir, to_dir

def test_load_processed_files(temp_dirs):
    """Test that we can load processed files from the log"""
    from_dir, to_dir = temp_dirs
    log_file = os.path.join(to_dir, "extraction_log.txt")
    
    # Create a test log file
    with open(log_file, "w") as f:
        f.write("Extraction Log\n")
        f.write("====================\n")
        f.write("Successful Files:\n")
        f.write("test1.pdf\n")
        f.write("\nFailed Files:\n")
        f.write("test2.pdf\n")
    
    processed_files = load_processed_files(log_file)
    assert "test1.pdf" in processed_files
    assert "test2.pdf" not in processed_files

def test_main_skips_processed_files(temp_dirs, mocker):
    """Test that main() skips already processed files"""
    from_dir, to_dir = temp_dirs
    
    # Create a mock that doesn't raise exceptions
    def mock_extract(path):
        return "Mocked text"
    
    # Mock extract_text_from_pdf to avoid actual PDF processing
    mock_extract = mocker.patch('pdf_extractor.extract_pdfs.extract_text_from_pdf', 
                               side_effect=mock_extract)
    
    # First run - should process both files
    main(from_dir, to_dir, None)
    assert mock_extract.call_count == 2
    
    # Second run - should skip both files
    mock_extract.reset_mock()
    main(from_dir, to_dir, None)
    assert mock_extract.call_count == 0
    
    # Verify log file contains both successful files
    with open(os.path.join(to_dir, "extraction_log.txt"), 'r') as log:
        content = log.read()
        assert "test1.pdf" in content
        assert "test2.pdf" in content 
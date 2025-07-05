import PyPDF2
import docx
import logging
from werkzeug.utils import secure_filename
from config import Config

logger = logging.getLogger(__name__)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file with better error handling."""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF")
            
        return text.strip()
        
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise ValueError(f"Failed to extract text from PDF: {str(e)}")

def extract_text_from_docx(docx_file):
    """Extract text from DOCX file."""
    try:
        doc = docx.Document(docx_file)
        text = ""
        
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        if not text.strip():
            raise ValueError("No text could be extracted from the DOCX file")
            
        return text.strip()
        
    except Exception as e:
        logger.error(f"Error extracting text from DOCX: {str(e)}")
        raise ValueError(f"Failed to extract text from DOCX: {str(e)}")

def extract_text_from_txt(txt_file):
    """Extract text from TXT file with encoding detection."""
    try:
        # Try UTF-8 first
        text = txt_file.read().decode('utf-8')
        if not text.strip():
            raise ValueError("The text file appears to be empty")
        return text.strip()
        
    except UnicodeDecodeError:
        # Fallback to other encodings
        txt_file.seek(0)
        try:
            text = txt_file.read().decode('latin-1')
            if not text.strip():
                raise ValueError("The text file appears to be empty")
            return text.strip()
        except Exception as e:
            logger.error(f"Error reading text file: {str(e)}")
            raise ValueError("Failed to read text file - unsupported encoding")

def extract_text_from_file(file):
    """Extract text from uploaded file based on its extension."""
    if not file or not file.filename:
        raise ValueError("No file provided")
    
    filename = secure_filename(file.filename)
    file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    
    if file_extension == 'txt':
        return extract_text_from_txt(file)
    elif file_extension == 'pdf':
        return extract_text_from_pdf(file)
    elif file_extension == 'docx':
        return extract_text_from_docx(file)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

def sanitize_text(text):
    """Sanitize extracted text for processing."""
    if not text:
        return ""
    
    # Remove excessive whitespace and normalize
    import re
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Limit text length to prevent API issues
    max_length = 8000  # Reasonable limit for resume text
    if len(text) > max_length:
        text = text[:max_length] + "..."
        logger.warning(f"Text truncated to {max_length} characters")
    
    return text

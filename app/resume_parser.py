import docx
import PyPDF2
from typing import Union

def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX resume"""
    doc = docx.Document(file_path)
    return " ".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF resume"""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_resume_text(file_path: str) -> Union[str, None]:
    """Auto-detect and extract text from resume (PDF or DOCX)"""
    if file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    else:
        return None
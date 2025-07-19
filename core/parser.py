from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import os


def parse_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def parse_docx_file(filepath):
    doc = Document(filepath)
    return "\n".join([p.text for p in doc.paragraphs])


def parse_pdf_file(filepath):
    return extract_pdf_text(filepath)


def parse_file(filepath):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == ".txt":
        return parse_text_file(filepath)
    elif ext == ".pdf":
        return parse_pdf_file(filepath)
    elif ext == ".docx":
        return parse_docx_file(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

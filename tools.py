import pymupdf4llm
import requests

def pdf_to_markdown(pdf_path):
    md_text = pymupdf4llm.to_markdown(pdf_path)
    return md_text

def read_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    return markdown_text   

def markdown_to_text(markdown_text):
    with open(markdown_text, "r", encoding="utf-8") as f:
        text = f.read()
    return text
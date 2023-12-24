import tiktoken  # Assuming 'tiktoken' is the correct library name
import os
import random
import PyPDF2

def pdf_to_text(file_path):
    """
    Convert a PDF file to a text string.
    """
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def count_tokens(text):
    """
    Count tokens in a text string.
    """
    # Splitting the text into tokens (words)
    tokens = text.split()
    return len(tokens)

# Example usage
file_path = 'District_12/str2020-Ohio-45.pdf'  # Replace with your PDF file path
pdf_text = pdf_to_text(file_path)
token_count = count_tokens(pdf_text)
print(f"Total tokens: {token_count}")
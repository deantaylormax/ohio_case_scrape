import os
import pandas as pd
import tiktoken
import PyPDF2

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

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
            text += page.extract_text() if page.extract_text() else ""
    return text

def process_directory(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            text = pdf_to_text(file_path)
            tokens = num_tokens_from_string(text, "cl100k_base")
            case_no = os.path.splitext(filename)[0]
            data.append({'case_no': case_no, 'tokens': tokens})
    return pd.DataFrame(data)

# Replace 'your_directory_path' with the path to the directory containing the PDFs
directory_path = 'District_12'
df = process_directory(directory_path)
# print(df.head())
# Save the DataFrame to a CSV file
df.to_csv(f'all_files_tokens_{directory_path}.csv', index=False)
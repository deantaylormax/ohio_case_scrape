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
            text += page.extract_text()
    return text

test_text = pdf_to_text('District_8/str2023-Ohio-2299.pdf')

total_tokens = num_tokens_from_string(test_text, "cl100k_base")
print(f'these are the total tokens {total_tokens}')
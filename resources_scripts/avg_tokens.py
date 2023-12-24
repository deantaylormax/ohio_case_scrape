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
            text += page.extract_text() if page.extract_text() else ""
    return text

def count_tokens(text):
    """
    Count tokens in a text string.
    """
    tokens = text.split()
    return len(tokens)

# Directory containing PDF files
directory_path = 'District_4/2023'  # Replace with your directory path
# Get a list of PDF files in the directory
pdf_files = [file for file in os.listdir(directory_path) if file.endswith('.pdf')]
# Randomly select five PDF files
selected_pdfs = random.sample(pdf_files, 20) if len(pdf_files) >= 5 else pdf_files
# print(selected_pdfs)
# # Initialize variables for total tokens and counts
total_tokens = 0
file_counts = {}

# Process each selected PDF
for pdf in selected_pdfs:
    file_path = os.path.join(directory_path, pdf)
    pdf_text = pdf_to_text(file_path)
    token_count = count_tokens(pdf_text)
    file_counts[pdf] = token_count
    total_tokens += token_count

# Calculate the average number of tokens
average_tokens = total_tokens / len(selected_pdfs)
# Print the token count for each file and the average
for pdf, count in file_counts.items():
    print(f"Total tokens in {pdf}: {count}")
print(f"\nAverage number - selected PDFs: {average_tokens}\n")

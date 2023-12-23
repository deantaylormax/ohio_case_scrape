#import the embed_api_key from the .env file
from dotenv import load_dotenv
import os

load_dotenv()
embed_api_key = os.getenv('EMBED_API_KEY')

import PyPDF2
from openai import OpenAI

client = OpenAI(api_key=embed_api_key)

def pdf_to_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() if page.extract_text() else ""
    return text

def get_embeddings(text):
    
    response = client.embeddings.create(input=text, engine="text-embedding-ada-002")
    return response['data'][0]['embedding']

def process_directory(directory):
    embeddings = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            text = pdf_to_text(file_path)
            embedding = get_embeddings(text)
            embeddings[filename] = embedding
    return embeddings

# Replace 'your_directory_path' with the path to the directory containing the PDFs
directory_path = 'District_1/2005'
embeddings = process_directory(directory_path)
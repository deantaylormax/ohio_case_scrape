import os
import json
import warnings
from dotenv import load_dotenv
import pinecone
from openai import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import streamlit as st

load_dotenv()
def initialize_clients():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = "us-east-1-aws"
    openai_client = OpenAI()
    embed_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    index = pinecone.Index("doc-prod-test")
    return openai_client, embed_model, index
def query_similar_documents(client, embed, index, query, top_k=5):
    try:
        res = client.embeddings.create(input=[query], model=embed.model)
        if res and res.data:
            embeddings = res.data[0].embedding
            results = index.query(vector=embeddings, top_k=top_k, include_metadata=True)
            return results
    except Exception as e:
        print(f"Error during query: {e}")
        return None
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

st.title("Legal Case Search")

col1, col2 = st.columns([2,1])
with col1:
    query = st.text_area("Enter the facts of your legal matter here:", height=200)
with col2:
    top_k = st.radio("Maximum results", [5, 10, 15])
    top_k = int(top_k)

search_button = st.button("Search")
if search_button and query:
    openai_client, embed_model, pinecone_index = initialize_clients()
    results = query_similar_documents(openai_client, embed_model, pinecone_index, query, top_k)
    if results:
        search_complete = st.write("Search complete!")
        for item in results['matches']: #make two columns where the first is narrower than the second
            col1, col2 = st.columns([1, 2])
            with col1:
                metadata = item['metadata']
                case_no = metadata['case_no']
                district = metadata['district']
                url = metadata['url']
                text = metadata['text']
                score = item['score']
                score = "{:.2%}".format(score)
                st.write(f"Case No: {case_no}")
                st.write(f"Appellate District: {district}")
                st.write(f"Similarity Score: {score}")
            with col2:
                st.write(f"Case Text: {text}")
                text = f"[Click Here To Download The Official Opinion]({url})"
                st.markdown(text)
                st.markdown("---")
elif search_button and not query:
    error_notice = st.write("Please enter the facts of your legal matter and click search.")
import os
import json
import warnings
from dotenv import load_dotenv
import pinecone
from openai import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import streamlit as st
load_dotenv()

st.title("Legal Case Search")

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

#MAIN APP
def main():
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
    # elif search_button and not query:
    #     error_notice = st.write("Please enter the facts of your legal matter and click search.")

# Function to parse the credentials from the .env file
def get_credentials():
    user_credentials = {}
    for i in range(1, 5):  # Adjust based on the number of users
        username = os.getenv(f"USER{i}")
        password = os.getenv(f"PASSWORD{i}")
        if username and password:
            user_credentials[username] = password
    return user_credentials
users = get_credentials()

# Function to verify credentials
def verify_credentials(username, password, users):
    return username in users and users[username] == password

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'attempted_login' not in st.session_state:
    st.session_state.attempted_login = False

st.sidebar.title("Login")

if not st.session_state.get('logged_in', False):
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        st.session_state.attempted_login = True
    # Check against both sets of credentials
    if verify_credentials(username, password, users):
        # st.session_state.logged_in = True
        st.success("Logged in successfully!")
        main()
    else:  # This else belongs to the for loop, not the if statement
        if st.session_state.attempted_login:
            st.error("Incorrect username or password")
else:
    # User is logged in, show logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.attempted_login = False
        st.session_state.user_role = None
        st.rerun()  # Use experimental_rerun for the latest versions of Streamlit

# def initialize_clients():
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
#     PINECONE_ENV = "us-east-1-aws"
#     openai_client = OpenAI()
#     embed_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
#     pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
#     index = pinecone.Index("doc-prod-test")
#     return openai_client, embed_model, index
# def query_similar_documents(client, embed, index, query, top_k=5):
#     try:
#         res = client.embeddings.create(input=[query], model=embed.model)
#         if res and res.data:
#             embeddings = res.data[0].embedding
#             results = index.query(vector=embeddings, top_k=top_k, include_metadata=True)
#             return results
#     except Exception as e:
#         print(f"Error during query: {e}")
#         return None
with warnings.catch_warnings():
    warnings.simplefilter("ignore")


# def main():
#     col1, col2 = st.columns([2,1])
#     with col1:
#         query = st.text_area("Enter the facts of your legal matter here:", height=200)
#     with col2:
#         top_k = st.radio("Maximum results", [5, 10, 15])
#         top_k = int(top_k)

#     search_button = st.button("Search")
#     if search_button and query:
#         openai_client, embed_model, pinecone_index = initialize_clients()
#         results = query_similar_documents(openai_client, embed_model, pinecone_index, query, top_k)
#         if results:
#             search_complete = st.write("Search complete!")
#             for item in results['matches']: #make two columns where the first is narrower than the second
#                 col1, col2 = st.columns([1, 2])
#                 with col1:
#                     metadata = item['metadata']
#                     case_no = metadata['case_no']
#                     district = metadata['district']
#                     url = metadata['url']
#                     text = metadata['text']
#                     score = item['score']
#                     score = "{:.2%}".format(score)
#                     st.write(f"Case No: {case_no}")
#                     st.write(f"Appellate District: {district}")
#                     st.write(f"Similarity Score: {score}")
#                 with col2:
#                     st.write(f"Case Text: {text}")
#                     text = f"[Click Here To Download The Official Opinion]({url})"
#                     st.markdown(text)
#                     st.markdown("---")
#     elif search_button and not query:
#         error_notice = st.write("Please enter the facts of your legal matter and click search.")
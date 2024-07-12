import streamlit as st
import asyncio
import os
from embedchain import App

# Function to initialize Embedchain app
async def initialize_app(api_key):
    return App.from_config(config_path="config.yaml", api_key=api_key)

# Function to query Embedchain
async def query_answer(app, question):
    return await app.query(question)

def main():
    st.title('Embedchain Query App')
    
    # Ask user for Embedchain API key
    api_key = st.text_input('Enter your Embedchain API key:')
    
    # Ask user for question
    question = st.text_area('Enter your question:')
    
    # Initialize Embedchain app and query when both API key and question are provided
    if st.button('Query') and api_key and question:
        st.write('Fetching answer...')
        try:
            app = asyncio.run(initialize_app(api_key))
            result = asyncio.run(query_answer(app, question))
            st.write(f'**Question:** {question}')
            st.write(f'**Answer:** {result}')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

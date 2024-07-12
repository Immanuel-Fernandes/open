import streamlit as st
from embedchain import App

# Function to initialize Embedchain app
async def initialize_app(api_key):
    return await App(api_key=api_key)

# Function to query Embedchain
async def query_answer(app, question):
    return await app.query(question)

def main():
    st.title('Embedchain Query App')
    
    # Ask user for Embedchain API key
    api_key = st.text_input('Enter your Embedchain API key:')
    
    # Ask user for question
    question = st.text_area('Enter your question:')
    
    # Initialize Embedchain app when both API key and question are provided
    if st.button('Query') and api_key and question:
        st.write('Fetching answer...')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        app = loop.run_until_complete(initialize_app(api_key))
        result = loop.run_until_complete(query_answer(app, question))
        st.write(f'**Question:** {question}')
        st.write(f'**Answer:** {result}')

if __name__ == '__main__':
    main()

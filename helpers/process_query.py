from snowflake.core import Root
from snowflake.snowpark.session import Session
from snowflake.cortex import Complete
import streamlit as st
from dotenv import load_dotenv
import os

from helpers.base_prompt import get_base_prompt
from helpers.message_cards import create_human_message_card, stream_static_string

load_dotenv()

def get_top_k_results(root, query, k):
    benefits_service = root.databases['benefits_db'].schemas['benefits'].cortex_search_services['benefits_service']
    
    top_k_results = benefits_service.search(
        query = query,
        columns = [
            'chunk',
            'file_url',
            'relative_path'
        ],
        filters = {'@and': [{'@eq': {'language': 'English'}}]},
        limit = k
    )

    return top_k_results

def generate_response(query):
    connection_params = {
        "account":  os.getenv('SNOWFLAKE_ACCOUNT'),
        "user": os.getenv('SNOWFLAKE_USER'),
        "password": os.getenv('SNOWFLAKE_PASSWORD'),
        "role": os.getenv('SNOWFLAKE_ROLE'),
        "database": os.getenv('SNOWFLAKE_DATABASE'),
        "schema": os.getenv('SNOWFLAKE_SCHEMA'),
        "warehouse": os.getenv('SNOWFLAKE_WAREHOUSE')
    }

    snowpark_session = Session.builder.configs(connection_params).create()
    root = Root(snowpark_session)

    k = 10
    prompt_context = get_top_k_results(root, query, k)

    prompt = get_base_prompt(prompt_context, query)

    response = Complete("mistral-large2", prompt, session = snowpark_session)

    return response

def process_query(query_text: str):
    # to record chat history
    st.session_state.messages.append({
        'role': 'human',
        'content': query_text
    })

    create_human_message_card(query_text) # display human chat

    # query chunks and generate response
    if st.session_state.messages[-1]['role'] != 'ai':
        with st.spinner('Generating response...'):
            response = generate_response(query_text)

        # st.write('Some text') # for debugging purpose
        stream_static_string(response) # add typing effect here
        
        st.session_state.messages.append({
            'role': 'ai',
            'content': response
        })
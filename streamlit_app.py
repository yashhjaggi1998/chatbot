import streamlit as st

from helpers.process_query import process_query
from helpers.message_cards import create_ai_message_card, create_human_message_card
from helpers.load_styles import load_css_styles
from helpers.sidebar import display_sidebar
from helpers.theme import theme

def clear_chat_history():
    st.session_state.messages = [
        {
            'role': 'ai',
            'content': 'How may I help you'
        }
    ]
    
def display_messages():
    for message in st.session_state.messages:
        if message['role'] == 'ai':
            create_ai_message_card(message['content'])
        else:
            create_human_message_card(message['content'])
    
def init_chat_history():
    if 'messages' not in st.session_state:
        clear_chat_history()

company_options = ('37signals', 'gitlab')

# -------------------------- Main Code --------------------------
# Show title and description.
st.set_page_config(page_title = '💬 Benefits Guide')

if 'selected_company' not in st.session_state:
    st.session_state.selected_company = ''

display_sidebar()

if st.session_state.selected_company == '':
    st.write(st.session_state.selected_company)
    selected_company = st.selectbox("Please select your company before we can assist you!", company_options)
    st.session_state.selected_company = selected_company
else:
    load_css_styles(theme)
    init_chat_history()
    display_messages()

    if prompt := st.chat_input('Bring it on...'):
        process_query(prompt)
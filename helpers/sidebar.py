import streamlit as st

company_options = {
    '37signals': 0, 
    'gitlab': 1
}

def display_sidebar():
    with st.sidebar:
        st.title('Benefits Guide')
        
        if st.session_state.selected_company != '':
            selected_company = st.selectbox(
                label = "Change company", 
                options = company_options,
                index = company_options[st.session_state.selected_company]
            )
            st.session_state.selected_company = selected_company
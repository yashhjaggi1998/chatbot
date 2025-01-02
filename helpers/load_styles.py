import streamlit as st

def load_css_styles(theme):
    st.markdown(f"""
        <style>
            .message-wrapper {{
                display: flex;
                align-items: flex-start;
                gap: 0.6rem;
                margin-top: 0.8rem;
                margin-bottom: 0.8rem;
            }}
            .message-wrapper.human {{
                flex-direction: row-reverse;
            }}
                
            .avatar {{
                display: flex;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
                width: 2rem;
                height: 2rem;
                border-radius: 2rem;
            }}
            .ai-avatar {{
                background: {theme['colors']['light-grey']};
            }}
            .human-avatar {{
                background: {theme['colors']['light-primary']};
                color: {theme['colors']['black']};
            }}

            .message {{
                background: {theme['colors']['white']};
                padding: 0.6rem;
                border-radius: 0.5rem;
                box-shadow: 2px 2px 4px rgba(5, 5, 5, 0.2);
                max-width: 100%;
                line-height: 1.5;
            }}
            .human .message {{
                background: {theme['colors']['light-primary']};
            }}
            .ai .message {{
                background: {theme['colors']['light-grey']};
            }}
        </style>
    """, unsafe_allow_html=True)
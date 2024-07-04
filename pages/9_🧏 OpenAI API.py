import streamlit as st
from streamlit_extras.stateful_button import button
from utils import tab_openai, streamlit_components, streamlit_docs

streamlit_components.streamlit_ui('🦣 OpenAI API')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["General", "Text Completion", "Vision", "", ""])

with tab1:  
    if button("Click to Continue", key="button1"):
        completion = tab_openai.openai_general('g')
        st.write(completion)
with tab2:  
    if button("Click to ", key="bu2"):
        tab_openai.openai_textcompletion()
with tab3: 
    if button("Click to 1Continue", key="button12"):
        tab_openai.openai_vision()

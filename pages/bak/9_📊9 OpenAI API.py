import streamlit as st
from utils import st_def, tab_openai
st_def.st_logo(title = "👋 OpenAI API!", page_title="ChatGPT",)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["General", "Text Completion", "Vision", "Mongo", "PostgreQL"])

with tab1:  tab_openai.openai_general()
with tab2:  tab_openai.openai_textcompletion()
with tab3:  tab_openai.openai_vision()
with tab4:  tab_openai.openai_mongo()
with tab5:  tab_openai.openai_postgreql()

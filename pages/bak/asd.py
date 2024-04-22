import streamlit as st
from utils import st_def, tab_st
st_def.st_logo(title = "👋 Streamlit!", page_title="Streamlit",)

tab1, tab2, tab3 = st.tabs(["PostgreQL", "All in One", "Mongo"])

with tab1:  tab_st.st_core()
with tab2:  tab_st.st_allin1()
with tab3:  tab_st.st_mongo()

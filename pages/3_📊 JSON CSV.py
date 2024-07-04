import streamlit as st, re
from utils import st_def, tab_db, tab_json
st_def.st_logo(title = "👋 JSON",)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["General", "JSON", "Save to JSON, CSV", "Mongo", "PostgreQL"])

with tab1:  tab_json.db_general()
with tab2:  tab_json.db_JSON()
with tab3:  tab_json.db_jsoncsv()

import streamlit as st
from utils import st_def, tab_db
st_def.st_logo(title = "👋 Database Prototype!")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["General", "mySQL-py", "mySQL-Oracle", "Mongo", "PostgreQL"])

with tab1:  tab_db.db_general()
with tab2:  tab_db.db_mysql1()
with tab3:  tab_db.db_mysql2()
with tab4:  tab_db.db_mongo()
with tab5:  tab_db.db_postgreql()

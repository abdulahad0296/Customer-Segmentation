import streamlit as st
import sqlite3
import pandas as pd

def run_query(query):
    conn = sqlite3.connect("customers.db")
    df=pd.read_sql_query(query,conn)
    conn.close()
    
    return df




import streamlit as st
from run_query import run_query, queries

st.title("Customer Segmentation & Market Basket Analysis")

option=st.sidebar.selectbox("Select the query you wish to run:",list(queries.keys()))

st.subheader(option)
df=run_query(queries[option])

st.dataframe(df)
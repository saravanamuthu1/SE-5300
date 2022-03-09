from calendar import TUESDAY
from pip import main
import streamlit as st
import pandas as pd
import numpy as np
st.title("my data app")
st.write(""" upload csv file """)
todrop=[]
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    df.fillna(0)
    st.write(df.describe())
    st.write("check the colomn to be deleted")
    for column in df.columns:
        st.checkbox(column)
        st.line_chart(df[column])
    st.dataframe(df)
    text_input=st.text_input("enter the column to e deleted")
    if(type(text_input) == str):
        df.drop(columns=[st.text_input("enter the column to be deleted")],axis=1,inplace=True)
        st.write("column is deleted")
        st.dataframe(df)
    else:
        st.write("column not found")


import streamlit as st
import pandas as pd
import numpy as np

#upload file 
st.title("my data app")
st.write(""" upload csv file """)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df1 = pd.read_csv(uploaded_file)
    #fill data with zeros for null values
    df1=df1.fillna(0)
"""
check box function
"""
def check_box():
    """
    check box function
    """
    if st.checkbox('describe the data'):
        st.subheader('desscribe values')
        st.write(df1.describe())
    if st.checkbox('show raw data'):
        st.subheader('raw data')
        st.write(df1)
        st.write("check the colomn to be deleted")
    st.write("columns in the  data")
    for column in df1.columns:
        st.checkbox(column)
    for column in df1.columns:
        st.line_chart(df1[column])
"""
   delete column function
"""
def delete_column():
    """
     delete column function
    """
    text_input1=st.text_input("do you want to delete columns")
    if(text_input1 == "yes"):
        if(type(text_input1) == str):
            df1.drop(columns=[st.text_input("enter the column to be deleted")],axis=1,inplace=True)
            st.write("column is deleted")
            st.dataframe(df1)
        else:
            st.write("column not found")
if __name__ =="__main__":
    check_box()
    delete_column()

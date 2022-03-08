from pip import main
import streamlit as st
import pandas as pd
import numpy as np
st.title("my data app")
st.write(""" upload csv file """)
todrop=[]
def __init__(self,dataframe):
    self.dataframe=dataframe
def filldata(self):
    self.dataframe.fillna(0)
    self.dataframe.duplicated()
    st.write(self.dataframe.describe())
    st.write("colum name in the csv file")
    for column in self.dataframe.columns:
        st.markdown(column)
    num_input=st.number_input("enter the number of colums to ve deleted",min_value=0,max_value=len(self.dataframe.columns),step=1)
    for i in range(num_input):
        text_input=st.text_input("enter the column to be deleted")
        todrop.append(text_input)
if __name__ =="__main__":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
    filldata()


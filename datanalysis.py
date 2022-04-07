import pandas as pd
import numpy as np
import os


def get_data(data):
   dataframe = pd.read_csv(data)
   return dataframe

def clean_data(data):
   data.dropna(axis=0,inplace=True)
   return data

def get_size(data):
    return data.size

def get_columns(data):
    return data.columns

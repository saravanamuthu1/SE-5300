from ast import Store
from flask import Flask,render_template,request,url_for,redirect
from flask_uploads import UploadSet,configure_uploads,IMAGES,DATA,ALL
from werkzeug.datastructures import  FileStorage
import os
import datetime
import time


# EDA Packages
import pandas as pd 
import numpy as np 
app = Flask(__name__)
files = UploadSet("files",ALL)
app.config['UPLOADED_FILES_DEST']=' static/storage'
configure_uploads(app,files)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/uploadFiles', methods=['GET','POST'])
def uploadFiles():
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename=file.filename
        file.save(os.path.join('static/storage',filename))
        df=pd.read_csv(os.path.join('static/storage',filename))
        size=df.size
        columns=df.columns
        df=df.dropna()
        val=df.describe()
        if request.method == 'POST':
            li=request.form.getlist("mycheckbox")
            for i in li:
                df.drop(i,axix=1,inplace=True)
            column=df.columns
    return render_template('index.html',filename=filename,size=size,columns=columns,column=column)




if __name__ == "__main__":
    app.run(debug=True)

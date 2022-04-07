from ast import Store
from flask import Flask,render_template,request,url_for,redirect
from flask_uploads import UploadSet,configure_uploads,IMAGES,DATA,ALL
from werkzeug.datastructures import  FileStorage
import os
import datetime
import time
from dataanalysis import get_data,clean_data,get_size,get_columns

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
        df=get_data(os.path.join('static/storage',filename))
        df=clean_data(df)
        data_size=get_size(df)
        column_names=get_columns(df)
    return render_template('index.html',filename=filename,data_size=data_size,column_names=column_names)




if __name__ == "__main__":
    app.run(debug=True)


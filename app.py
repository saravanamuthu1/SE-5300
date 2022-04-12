from fileinput import filename
from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,ALL,DATA
from werkzeug import secure_filename


app = Flask(__name__)
Bootstrap(app)

# Configuration

files=UploadSet('files',ALL)
app.config['UPLOADED_FILES_DEST']='static/storage'
configure_uploads(app,files)

import os
import datetime
import time


#EDA Packages
import pandas as pd 
import numpy as np 


# ML Packages

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/datauploads', methods=['GET','POST'])
def datauploads():
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename =secure_filename(file.filename)
        file.save(os.path.join('static/storage',filename))
        df=pd.read_csv(os.path.join('static/storage',filename))
        df_shape=df.shape
        df_size=df.size
        df_columns=df.columns
        df_head=df.head(10)
    return render_template('details.html',filename=filename,df_table=df,df_shape=df_shape,df_size=df_size,df_columns=df_columns,df_head=df_head)


if __name__ == '__main__':
	app.run(debug=True)


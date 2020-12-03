from flask import Flask, request, redirect
import json
import requests
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename
load_dotenv()
app=Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="uploadFile"><input type=file name=uploadingFile><input type=submit></form>'''

@app.route('/uploadFile', methods=['POST'])
def uploadImage():
    CLIENT_ID=os.getenv('client_id')
    CLIENT_SECRET=os.getenv('client_secret')
    f = request.files['uploadingFile']
    Filename=f.filename
    try:
        f.save(os.path.join('./uploaded',secure_filename(Filename)))
    except:
        os.mkdir(os.path.join('.', 'uploaded'))
        f.save(os.path.join('./uploaded',secure_filename(Filename)))
    f=open(os.path.join('./uploaded', secure_filename(Filename)), "rb")
    para={
        "title": Filename,
        "parents": [{"id": "root"}]
    } 
    files = {'data':("metadata", json.dumps(para), "application/json; charset=UTF-8"), "file": f}
    REFRESH_TOKEN=os.getenv('refresh_token')
    ACCESS_TOKEN=json.loads((requests.post(f'https://oauth2.googleapis.com/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&refresh_token={REFRESH_TOKEN}&grant_type=refresh_token')).content)['access_token']
    headers={'Authorization': "Bearer "+ACCESS_TOKEN}
    response = requests.post("https://www.googleapis.com/upload/drive/v2/files?uploadType=multipart", headers=headers, files=files)
    print(response)
    return f'Done with response code : <strong>{response.status_code}</strong> ! <a href="/">Upload Again</a>'

app.run(host="0.0.0.0", debug=True, port="3000")

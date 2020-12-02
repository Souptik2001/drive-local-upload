from flask import Flask, request, redirect
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)

@app.route('/')
def index():
    CLIENT_ID=os.getenv('client_id')
    REDIRECT_URL=os.getenv('redirect_url')
    return f'You will get you access and authorization token here. Get you access token here : <a href="https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/drive&access_type=offline&include_granted_scopes=true&response_type=code&state=state_parameter_passthrough_value&redirect_uri={REDIRECT_URL}&client_id={CLIENT_ID}">Sign in with google.</a>'
@app.route('/tokens')
def tokens():
    CLIENT_ID=os.getenv('client_id')
    CLIENT_SECRET=os.getenv('client_secret')
    REDIRECT_URL=os.getenv('redirect_url')
    auth_code=request.args.get('code')
    access_token=request.args.get('access_token')
    refresh_token=request.args.get('refresh_token')
    if access_token!=None:
        return f'You access token is : <strong>{access_token}</strong> and refresh token is : <strong>{refresh_token}</strong>'
    else:
        response = requests.post(f'https://oauth2.googleapis.com/token?code={auth_code}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri={REDIRECT_URL}&grant_type=authorization_code')
        creds = json.loads(response.content)
        #return f'ACCESS_TOKEN : <strong>{creds["access_token"]}</strong> and REFRESH_TOKEN : <strong>{creds["refresh_token"]}</strong>'
        return f'''
            <html lang="en">
                <head>
                    <meta charset="utf-8">

                    <title>TOKENS</title>
                    <meta name="description" content="">

                </head>
                <body>
                    ACCESS_TOKEN : {creds["access_token"]} and REFRESH_TOKEN : {creds["refresh_token"]}
                </body>
            </html>'''
@app.route('/secret/<name>')
def hello(name):
        return f'Welcome to secret page {name}'

app.run(debug=True, port="3000")

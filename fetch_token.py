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
    REFRESH_TOKEN=os.getenv('refresh_token')
    if(REFRESH_TOKEN==None):
        return f'You will get you access and authorization token here. Get you access token here : <a href="https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/drive&access_type=offline&include_granted_scopes=true&response_type=code&state=state_parameter_passthrough_value&redirect_uri={REDIRECT_URL}&client_id={CLIENT_ID}">Sign in with google.</a>'
    else:
        return 'You already have your refresh token. To get a new refresh token delete the refresh_token field manually from the .env file and restart the server.'
@app.route('/tokens')
def tokens():
    CLIENT_ID=os.getenv('client_id')
    CLIENT_SECRET=os.getenv('client_secret')
    REDIRECT_URL=os.getenv('redirect_url')
    auth_code=request.args.get('code')
    access_token=request.args.get('access_token')
    if access_token!=None:
        return f'You access token is : <strong>{access_token}</strong> and refresh token is : <strong>{refresh_token}</strong>'
    else:
        if(True):
            response = requests.post(f'https://oauth2.googleapis.com/token?code={auth_code}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri={REDIRECT_URL}&grant_type=authorization_code')
            creds = json.loads(response.content)
            credfile=open('./.env', 'a')
            credfile.write(f'\nrefresh_token={creds["refresh_token"]}')
            credfile.close()
            #return f'ACCESS_TOKEN : <strong>{creds["access_token"]}</strong> and REFRESH_TOKEN : <strong>{creds["refresh_token"]}</strong>'
            return f'''
                <html lang="en">
                    <head>
                        <meta charset="utf-8">

                        <title>TOKENS</title>
                        <meta name="description" content="">

                    </head>
                    <body>
                        Credentials stored.
                    </body>
                </html>'''
        else:
            return 'You already have your refresh token. To get a new refresh token delete the refresh_token field manually from the .env file.'
@app.route('/secret/<name>')
def hello(name):
        return f'Welcome to secret page {name}'

#app.run(debug=True, port="3000")
app.run(host="0.0.0.0", debug=True, port="3000")

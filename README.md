# File transfer mini server
## About
Here I decided to create a miniserver which can be run at any time we want to upload files to our google drive and also make a copy in our miniserver without creating any kind of login or third party stuff.
## Setup overview
So here I decided to use this in my android device. So, I installed termux[a terminal emulator for smartphones].
- To clone this repo install git by
```bash
pkg install git
```
- Next clone the repo -
```bash
git clone https://github.com/Souptik2001/drive-local-upload
```
## Setup credentials
- As instructed in [Google's oauht page](https://developers.google.com/adwords/api/docs/guides/authentication#create_a_client_id_and_client_secret) create a clientid and clientsecret[only..no need to create tokens right now]. 
- Paste those two fields in a .env file as directed in the example.env file. Don't get the refresh token line as it will be handled by the fetchtoken server.
## Setup server
- Install the dependencies by running 
```bash
pip install requirements.txt
```
- Get you access token by creating a server through fetchtoken.py and then performing as directed in the web app [localhost:3000]
- Next run the autodrive...py and then visit [minServerIp:3000] in the system from which you wish to upload a file.[Both devices should be on same network]
- That's it upload file as needed. You will also get the files in the uploaded folder of you miniserver.


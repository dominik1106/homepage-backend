from fastapi import FastAPI

import os, platform, subprocess
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

@app.get('/running')
async def running():
    #https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host = os.getenv('MCSERVER_IP_ADRESS')

    command = ['ping', param, '1', host]
    res = subprocess.call(command) == 0
    if res:
        return {'message', 'Server is running!'}
    return {'message', 'Server not running!'}
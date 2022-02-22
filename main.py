import imp
from ipaddress import ip_address
from fastapi import FastAPI

import os, platform, subprocess
from dotenv import load_dotenv
from wakeonlan import send_magic_packet

app = FastAPI()
load_dotenv()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}

    
def is_server_running():
    #https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host = os.getenv('MCSERVER_IP_ADRESS')

    command = ['ping', param, '1', host]
    return (subprocess.call(command) == 0)

@app.get('/running')
async def running():
    if is_server_running():
        return {'message', 'Server is running!'}
    return {'message', 'Server not running!'}

@app.post('/startserver')
async def start_server():

    #only try to start server if it isn't already running
    if not is_server_running():
        mac_adress = os.getenv('MCSERVER_MAC_ADRESS')
        ip_address = os.getenv('MCSERVER_IP_ADRESS')
        send_magic_packet(macs=mac_adress, ip_address=ip_address)
        return {'message', 'Send Magic Package! Check back in a Minute'}
from fastapi import FastAPI
from dotenv import load_dotenv
from minecraft import is_server_running, wake_on_lan, get_server_info

app = FastAPI()
load_dotenv()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}


@app.get('/running')
async def running():
    if is_server_running(): 
        return {'message', 'Server is running!'}

    return {'message', 'Server not running!'}


@app.post('/startserver')
async def start_server():
    if not is_server_running():
        wake_on_lan()
        return {'message', 'Send Magic Package! Check back in a Minute'}

    return {'message', 'Server is already running!'}

@app.get('/serverstatus')
async def server_status():
    #Need to format this
    info = get_server_info()
    return info
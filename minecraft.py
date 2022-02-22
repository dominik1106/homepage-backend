import os, platform, subprocess, socket
from wakeonlan import send_magic_packet
from mcstatus import MinecraftServer


#This regards to the server the minecraft server is running on
def is_server_running():
    #https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host = os.getenv('MCSERVER_IP_ADRESS')

    command = ['ping', param, '1', host]
    return (subprocess.call(command) == 0)

def wake_on_lan():
    mac_adress = os.getenv('MCSERVER_MAC_ADRESS')
    ip_address = os.getenv('MCSERVER_IP_ADRESS')
    send_magic_packet(macs=mac_adress, ip_address=ip_address)


#This regards to the ACTUAL minecraft server ie the software
def get_server_info():
    ip_address = os.getenv('MCSERVER_IP_ADRESS')
    port: int = os.getenv('MCSERVER_PORT')

    server = MinecraftServer(ip_address, port)

    try:
        info = server.status()
    except socket.gaierror:
        return "Invalid hostname"
    except socket.timeout:
        return "Request timed out"
    except ConnectionRefusedError:
        return "Connection refused"
    except ConnectionError:
        return "Connection error"
    except (IOError, ValueError) as e:
        return "Error pinging server: {}".format(e)

    return info
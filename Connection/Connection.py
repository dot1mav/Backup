import os
import socket

from shutil import which


class Connection(object):
    def __init__(self) -> None:
        if not(self.__is_tool('croc')):
            if self.__is_too('snap'):
                os.system("sudo apt-get update &> /dev/null")
                os.system("sudo apt-get install snapd -y")
            else:
                os.system("sudo snap install croc")

    def __is_tool(self, name: str) -> bool:
        return which(name) is not None

    def Srv_Connection(self, file_name: str) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        del s
        os.system(f'croc --relay "{ip}:7779" send {file_name}')

    def Clt_Connection(self, command: str) -> None:
        os.system(f'{command}')
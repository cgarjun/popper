import socket
import os
import subprocess

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    message = buf.decode("utf-8") 
    username = message.split(' ')[0]
    body = ' '.join(message.split(" ")[1:])

    if len(buf) > 0:
        # cmd = 'python3 /Users/arjun/Documents/code/popper/src/popper_gui.py --sender {0} --message "{1}" &'.format(username, body)
        # print(cmd)
        # os.system(cmd)
        cmd = 'python3 /Users/arjun/Documents/code/popper/src/popper_gui.py --sender {0} --message "{1}"'.format(username, body)
        sd = '/Users/arjun/Documents/code/popper/src/popper_gui.py --sender {0} --message "{1}"'.format(username, body)
        print(sd)
        subprocess.Popen([cmd], shell=True)
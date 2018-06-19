#!/usr/bin/env python3
import socket
import os
import subprocess
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(4096)
    print(buf)
    print(type(buf))
    message_data = pickle.loads(buf)
    if len(buf) > 0:
        username = message_data['username']
        body = message_data['body']
        cmd = 'python3 '
        cmd += '/Users/arjun/Documents/code/popper/src/popper_gui.py'
        cmd += '--sender {0} --message "{1}" --bgcolor {2}'.format(username, body, bgcolor)
        subprocess.Popen([cmd], shell=True)
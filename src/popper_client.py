#!/usr/bin/env python3
import socket
import os
import subprocess
import pickle
import argparse
import json


def find_port_number():
    popper_config = os.getenv('POPPER_CONFIG', None)
    if popper_config is not None:
        with open(popper_config, 'r') as cfile:
            config_dict = json.load(cfile)
            port_number = config_dict.get('port', None)
            if port_number is not None:
                return port_number
            else:
                raise IOError('port number missingin the config')
    else:
        raise IOError('POPPER_CONFIG not found')

def main(args):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_number = find_port_number()

    if args.port:
        port_number = args.port

    print(port_number)
    print(type(port_number))
    serversocket.bind(('localhost', port_number))
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
            bgcolor = message_data['bgcolor']
            cmd = 'popper_gui '
            cmd += '--sender {0} --message "{1}" --bgcolor {2}'.format(username, body, bgcolor)
            subprocess.Popen([cmd], shell=True)

if __name__ == '__main__':
    arguments = argparse.ArgumentParser("CLI to send message")
    arguments.add_argument('--port', type=int, default=None, help='port number to listen')
    args = arguments.parse_args()
    main(args)
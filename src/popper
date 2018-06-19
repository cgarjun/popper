#!/usr/bin/env python

import socket
import argparse
import getpass
import pickle
import json
import os


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

def find_user_host(username):
    host_config = os.getenv('POPPER_HOST_CONFIG_LIST', None)
    if host_config is not None:
        with open(host_config, 'r') as cfile:
            host_list = json.load(cfile)
            user_host = host_list.get(username, None)
            if user_host is not None:
                return user_host
            else:
                raise IOError('User hostname not found')
    else:
        raise IOError('POPPER_HOST_CONFIG_LIST not found')

def main(args):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    message_data = {}
    username = getpass.getuser()
    host_name = find_user_host(username)

    if host_name is None:
        raise UserWarning('Cannot find the user host')
    
    message_data['username'] = username
    message_data['body'] = args.message
    message_data['bgcolor'] = args.bgcolor

    data = pickle.dumps(message_data)

    port_number = find_port_number()

    clientsocket.connect((host_name, port_number))
    clientsocket.send(data)

if __name__ == '__main__':
    arguments = argparse.ArgumentParser("CLI to send message")
    arguments.add_argument('--user', type=str, help='user id to send message to')
    arguments.add_argument('--message', type=str, help='message you want to send')
    arguments.add_argument('--bgcolor', type=str, default='grey', help='bgcolor of the gui')
    args = arguments.parse_args()
    main(args)
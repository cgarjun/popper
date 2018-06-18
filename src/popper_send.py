import socket
import getpass

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
username = getpass.getuser()
clientsocket.send('{0} hello this is my name'.format(username))
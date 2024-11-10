#How to create a client

import socket

soc=socket.socket()

soc.connect(('localhost', 9999))
print(soc.recv(1024).decode())
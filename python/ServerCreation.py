#How to create a server

import socket

soc = socket. socket()
print("Socket created successfully")

soc.bind(('localhost', 9999))
soc.listen(3)
print("Waiting for the connection ... ")

while True:
    conn,addr = soc. accept()
    print("connected with ", addr)
    conn. send ("Welcome to the Server". encode () )

import socket
from time import *
HOST='localhost'
PORT=5000
BUFSIZE=1024
ADDRESS=(HOST,PORT)
server=socket.socket()
server.bind(ADDRESS)
server.listen()
while True: #outer loop to accept connection from multiple clients
    print(" waiting for connection ...")
    (client,address)=server.accept()
    #print("...connecting from : ",address )
    client.send("Welcome to the server ".encode())
    client.send(bytes(ctime()+"\nHave a nice day ","ascii"))
    while True: #inner loop that send and receives (chat) with a client
        message=(client.recv(BUFSIZE)).decode()
        if not message:
            print("client is disconnected ")
            client.close()
            break
        else:
            print(message)
            message2=input(">")
            client.send(message2.encode())

#Practicing with Sockets

import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysocket.bind(('192.168.12.145',43210))
mysocket.listen(5)
print("TCP server running...")

while True:
    connectedsocket, connectedaddress = mysocket.accept()
    print("New connection from: " + str(connectedaddress))

import socket
import sys

HOST='127.0.0.1'
PORT=8888

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.sendall("hi")
data=s.recv(1024)
print 'Received data' + data
s.close()

import socket
import sys

HOST='127.0.0.1'
PORT=8888

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

s.listen(0)
print 'Starting server on' + str(HOST) + ':' + str(PORT) 
conn, addr=s.accept()

print 'Connected by', addr
testdata = conn.recv(1024)

print 'got data' + testdata

data="Hi you are connected"
try:
    conn.sendall(data)
    conn.sendall(data)
    conn.sendall(data)
except socket.error:
    print 'Send failed'
    sys.exit()

conn.close()
s.close()

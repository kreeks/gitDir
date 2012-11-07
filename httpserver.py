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
string = bytes.decode(testdata)
print 'data received' + string
request_method = string.split(' ')[0]
print "data is" + request_method
if request_method == 'GET':
        h = 'HTTP/1.1 200 OK\n'
        h += 'Connection: close\n\n'
        data = h.encode()
        data += "<html><body><p>HURRAY</p><p>Reached My Test Server</p></body></html>"
        print 'data begin sent' + data
        conn.send(data)
conn.close()
s.close()

import socket
import sys
import time
import os

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

while 1:
        conn, addr=s.accept()

        print 'Connected by', addr
        while 1:
                testdata = conn.recv(1024)
                if not testdata:
                        break
                string = bytes.decode(testdata)
                print 'data received' + string
                request_method = string.split(' ')[0]
                file_path = string.split(' ')[1]
                print "data is" + request_method
                print "file path" + file_path
                if request_method == 'GET':
                        h = 'HTTP/1.1 200 OK\n'
                        h += 'Connection: close\n\n'
                        data = h.encode()
                        data += "<html><body><p>HURRAY</p><p>Reached My Test Server</p>"
                        data += "<p>Current directory contents</p>"
                        print "path" + os.getcwd() + file_path
                        dirList=os.listdir(os.getcwd()+file_path)
                        for fname in dirList:
                                print "fname" + fname
                                if os.path.isdir(os.getcwd()+file_path+'/'+fname) == True:
                                        data += '<a href="' + fname + '">' + fname + "</a>"
                                        data += "</body></html>"
                                else:
                                        data += '<p>' + fname + '</p>'
                print 'data begin sent' + data
                conn.send(data)
        print 'closing connection to server'
        conn.close()

s.close()

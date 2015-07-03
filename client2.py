__author__ = 'shahryar_slg'

from socket import *
HOST = '127.0.0.1'
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:

    data = tcpCliSock.recv(BUFSIZ)
    print '>>>>Client 1 :',data
    data = raw_input('>>>>me: ')
    #print '>>>>Client2:  ',data
    tcpCliSock.send(data)
tcpCliSock.close()

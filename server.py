__author__ = 'shahryar_slg'

from socket import *
import re
HOST = ''
PORT = 21560
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(2)
clientsList=list()
p=re.compile(r'^quit$')
while True:
    print 'waiting for connection...'

    for i in range(1,3):
        print 'waiting for the client %s to be connected'%i
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr
        client=[tcpCliSock,addr]
        clientsList.append(client)

    while True:

        data=clientsList[0][0].recv(BUFSIZ)
        if data :
            clientsList[1][0].send(''.join(str(data)))



        data=clientsList[1][0].recv(BUFSIZ)
        if data :
            clientsList[0][0].send(''.join(data))

    clientsList[0][0].close()
    clientsList[1][0].close()
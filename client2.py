__author__ = 'shahryar_slg'

from socket import *
from time import sleep
HOST = '127.0.0.1'
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

Download_counter=0
while True:

    data = tcpCliSock.recv(BUFSIZ)
    print '>>>>Client 1 :',data



    data = raw_input('>>>>me: ')
    tcpCliSock.send(data)
    if data=="I want to download a file from Ur computer !":
        sleep(2) # to make sure server will run before client attemps to connect.
        PvPort=21570
        PvCliSock=socket(AF_INET,SOCK_STREAM)
        PvCliSock.connect((HOST,PvPort))

        Continue_Downloading=True
        while Continue_Downloading:
            path=raw_input("enter the path from which U want to download")
            PvCliSock.send(path)
            message=PvCliSock.recv(2048)
            print message
            while message=="Ooops !! the path U entered does not exist ... try again !":
                path=raw_input(">")
                PvCliSock.send(path)
                message=PvCliSock.recv(2048)


            num=PvCliSock.recv(2048)
            print "U can download %s files :"%num
            for i in range(int(num)):
                file=PvCliSock.recv(1024)
                print file,'\n'
            print "that's it"
            file_2_download_path=raw_input("type the one U want ...")
            PvCliSock.send(str(file_2_download_path))
            Download_counter+=1
            f=open('download %s'%Download_counter,'w')
            eleman=PvCliSock.recv(1024)
            while eleman:
                print "Receiving ..."
                f.write(eleman)
                eleman=PvCliSock.recv(4096)
            print "the file was successfully downloaded"
            f.close()









tcpCliSock.close()

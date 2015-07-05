__author__ = 'shahryar_slg'

from socket import *
from FileList import get_filepaths
import os

HOST = '127.0.0.1'
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = raw_input('>>>>me : ')
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    print ">>>>Client 2: ",data
    if data=="I want to download a file from Ur computer !":
        #now , Client should be a server itself
        PVPort=21570
        PvSerSock=socket(AF_INET,SOCK_STREAM)
        PvSerSock.bind((HOST,PVPort))
        PvSerSock.listen(1)
        PvCliSock,addr=PvSerSock.accept()

        Continue_Downloading=True
        while Continue_Downloading:
            #PvCliSock.send("enter the path from which U want to download")
            path=PvCliSock.recv(1024)
            is_path_valid=os.path.exists(path=path)
            while not is_path_valid:
                PvCliSock.send("Ooops !! the path U entered does not exist ... try again !")
                path=PvCliSock.recv(1024)
                is_path_valid=os.path.exists(path=path)
            if os.path.exists(path):
                PvCliSock.send("path is valid")


            print path
            files=get_filepaths(path)
            #PvCliSock.send("the files U can download are :")
            PvCliSock.send(str(len(files)))
            for file in files :
                PvCliSock.send(str(file))
            #PvCliSock.send("choose one of them ... and tell me which one u want to download")
            file_2_download_path=PvCliSock.recv(1024)
            print  "(s)he wants to download %s"%file_2_download_path


            wanted_file=open(file_2_download_path,'r')
            eleman=wanted_file.read()
            while eleman:
                print "Sending ..."
                PvCliSock.send(eleman)
                eleman=wanted_file.read()
            print "the file was succesfully sent"
            wanted_file.close()





tcpCliSock.close()

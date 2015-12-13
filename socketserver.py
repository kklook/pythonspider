#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import socket
import time
import threading
import webbrowser
class TcpLink(object):
    def __init__(self,url):
        self.data=None
        self.url=url
    def tcplink(self,sock,addr):
        while True:
            sock.send(self.url)
            time.sleep(3)
            self.data=sock.recv(1024)
            if(self.data!=None):
                print self.data
                break
        sock.close()
    def run(self):
        socketserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socketserver.bind(('0.0.0.0',9998))
        socketserver.listen(5)
        sock,addr=socketserver.accept()
        t=threading.Thread(target=self.tcplink,args=(sock,addr))
        t.start()
        return self.data


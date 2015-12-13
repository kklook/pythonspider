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
        sock.send(self.url)
        sock.close()
    def run(self):
        socketserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socketserver.bind(('0.0.0.0',9998))
        socketserver.listen(5)
        sock,addr=socketserver.accept()
        t=threading.Thread(target=self.tcplink,args=(sock,addr))
        t.start()


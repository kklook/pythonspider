#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import socket
import webbrowser
import time
class SocketClient(object):
    def __init__(self):
        self.data=None
    def run(self):
        while True:
            time.sleep(1)
            socketclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                socketclient.connect(('127.0.0.1',9998))
            except socket.error, e:
                print '服务器未上线'
                continue
            webbrowser.open_new_tab(socketclient.recv(1024))
s=SocketClient()
s.run()

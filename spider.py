#! /usr/bin/evn python evn
# -*- coding:utf-8 -*-
from urllib2 import urlopen
import urllib2
import re
import os
from taobao import Taobao
class Spider(object):
    def __init__(self):
        self.tao=Taobao()
        self.tao.main()
        self.u='http://mm.taobao.com/json/request_top_list.htm?page='
        self.rule_1='<div class="list-item">.*?<div class="pic-word">.*?<a href="//(.*?)".*?<img src="//(.*?)".*?<a class="lady-name" .*?>(.*?)</a>'
        self.rule_2='<img.*?src="//(.*?)"'
        self.rule_3='<div class="mm-aixiu-content".*?">(.*?)<!--'
    def baseurl(self,i):
        return self.u+str(i)
    def read(self,url):
        req=urllib2.Request(url)
        url=urlopen(req)
        page=url.read().decode('gbk')
        #page=page.encode('utf-8')
        return page
    def compile(self,rule):
        RE=re.compile(rule,re.S)
        return RE
    def mkdir(self,path):
        path=path.strip()
        if os.path.exists(path):
            return False
        else:
            os.makedirs(path)
            return True
    def savePicutre(self,temp,path):
        path=path.strip()
        k=0
        for i in temp:
            print i
            url=urlopen('http://'+i)
            with open(path+'\\'+str(k)+'.jpg','wb') as f:
                f.write(url.read())
            k=k+1
    def load(self,start,end):
        if isinstance(start,int) and isinstance(end,int):
            for i in range(start,end):
                 item=re.findall(self.compile(self.rule_1),self.read(self.baseurl(i)))
                 for temp in item:
                     if self.mkdir(temp[2]):
                         p=self.tao.getpage('http://'+temp[0])
                         p=p.decode('gbk')
                         p=p.encode('gbk')
                         picpart=re.search(self.compile(self.rule_3),p)
                         print picpart.group(1)
                         pic=re.findall(self.compile(self.rule_2),picpart.group(1))
                         print pic
                         self.savePicutre(pic,temp[2])
                     else:
                         raise(Exception)
        else:
            raise(Exception)

t=Spider()
t.load(1,10)
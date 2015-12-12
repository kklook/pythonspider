#! /usr/bin/evn python evn
# -*- coding:utf-8 -*-
from urllib2 import urlopen
import urllib2
import re
u='http://mm.taobao.com/json/request_top_list.htm?page='
k=0
for temp in range(50):
    tu=u+str(temp)
    req=urllib2.Request(tu)
    url=urlopen(req)
    RE=re.compile('<img src="//(.*?)"',re.S)
    page=url.read().decode('gbk')
    item=re.findall(RE,page)
    for i in item:
        h='http://'+i
        img=urlopen(h)
        data=img.read()
        with open(str(k)+'.jpg','wb') as f:
            f.write(data)
        k=k+1

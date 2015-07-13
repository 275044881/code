# coding:utf-8
import re
import itertools
import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup
import xlrd
import xlwt
import socket
import urlparse
import jieba
import jieba.analyse
import sys
#鑾峰彇缃戦〉鍐呭
import pagecontext
from pagecontext import getcontext
data = getcontext("http://voiceofcgnpc/WebpartPage/InfoDetails20150515.aspx?itemid=8859&listsource=/Lists/List3/2015.aspx")
soup = BeautifulSoup(data)
tmp = soup.find('div',attrs ={'class':"detailOuter"})
seg_list = jieba.cut(tmp.get_text().encode('gb18030'), cut_all=False)
tags = jieba.analyse.extract_tags(tmp.get_text().encode('gb18030'), topK=20,withWeight=True)
for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
sys.exit(0)
test = ", ".join(seg_list)
f=open('out.txt','w')
print >>f,test
f.close()

wbk = xlwt.Workbook(encoding='gb18030')
sheet = wbk.add_sheet('sheet 1')
wbk.save('test.xls')
i=0
for url in link_list:
	if url is None:
		print "error"
		exit()
	else:
	#鑾峰彇url
		owner = urlparse.urlsplit(url.get('href'))
		print url.get_text().encode('gb18030'),url.get('href'),owner.netloc.split(':')[0]
		sheet.write(i,0,url.get_text().encode('gb18030'))
		sheet.write(i,1,url.get('href'))
	#获取主机IP地址
		sheet.write(i,2,socket.gethostbyname(owner.netloc.split(':')[0]))
		i = i+1
wbk.save('test.xls')
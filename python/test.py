#-*- coding:gb18030 -*-
import re
import itertools
import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup
import xlrd
import xlwt
import socket
import urlparse
#获取网页内容
import pagetaglist
from pagetaglist import gettaglist

link_list = gettaglist("http://cnp/SitePages/Default3.aspx",'div','a',{'class':"menuwrp"})
wbk = xlwt.Workbook(encoding='gb18030')
sheet = wbk.add_sheet('sheet 1')
wbk.save('test.xls')
i=0
for url in link_list:
	if url is None:
		print "error"
		exit()
	else:
	#分割URL
		owner = urlparse.urlsplit(url.get('href'))
		print url.get_text().encode('gb18030'),url.get('href'),owner.netloc.split(':')[0]
		sheet.write(i,0,url.get_text().encode('gb18030'))
		sheet.write(i,1,url.get('href'))
	#获取主机IP地址
		sheet.write(i,2,socket.gethostbyname(owner.netloc.split(':')[0]))
		i = i+1
wbk.save('test.xls')
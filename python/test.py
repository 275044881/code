# coding:utf-8
import re
import itertools
import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup
import xlrd
import xlwt
import socket
# 获取网页内容
print 'test'
r = requests.get("http://cnp/SitePages/Default3.aspx",auth=HttpNtlmAuth('domain\\p135036','~1qaz2wsx'))
data = r.text
soup = BeautifulSoup(data)
tmp = soup.find('div',attrs ={'class':"menuwrp"})
link_list = tmp.find_all('a')
# 利用正则查找所有连接
#link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
wbk = xlwt.Workbook(encoding='gb18030')
sheet = wbk.add_sheet('sheet 1')
wbk.save('test.xls')
i=0
for url in link_list:
	if url is None:
		print "error"
		exit()
	else:
		print url.get_text().encode('gb18030'),url.get('href')
		sheet.write(i,0,url.get_text().encode('gb18030'))
		sheet.write(i,1,url.get('href'))
		sheet.write(i,2,socket.gethostbyname(url.get('href')))
		i = i+1
wbk.save('test.xls')
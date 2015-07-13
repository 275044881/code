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
import sys
def getcontext(url,userid='domain\\p135036',pwd='~1qaz2wsx'):
#获取网页内容
	reload(sys)
	sys.setdefaultencoding('utf-8')
	r = requests.get(url,auth=HttpNtlmAuth(userid,pwd))
	return r.text
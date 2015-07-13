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
import pagecontext
from pagecontext import getcontext
def gettaglist(url,miantag,subtag,css):
	data = getcontext(url)
	soup = BeautifulSoup(data)
	tmp = soup.find(miantag,attrs =css)
	return tmp.find_all(subtag)


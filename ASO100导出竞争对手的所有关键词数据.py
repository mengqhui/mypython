#!/usr/local/bin/python
# -*- coding:utf-8 -*-
######ASO100�����������ֵ����йؼ�������
######���ߣ�����
######���ͣ�http://seofangfa.com
######ʱ�䣺2016-10-13

import re
import os
import json
import time,datetime
import requests
import sys
reload(sys)
from lxml import etree
sys.setdefaultencoding('utf-8')
import codecs	#Ϊ������gbk������ļ�
today = datetime.date.today()


headers = {

	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'AlexaToolbar-ALX_NS_PH':'AlexaToolbar/alx-4.0',
	'Cache-Control':'no-cache',
	'Cookie':'',###########�滻���Լ���cookie��Ϣ
	'DNT':'1',
	'Host':'aso100.com',
	'Pragma':'no-cache',
	'Proxy-Connection':'keep-alive',
	'Referer':'http://aso100.com/search?search=51job',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	}

f = open(unicode('APP������������-%s.txt'%(today),'utf-8'),'w')
c =0 
appList = [['������Ƹ','488033535'],['58ͬ��','480079300'],['ǰ������','415443644'],['��Ƹ','540996859'],['����','1021464186'],['bossֱƸ','887314963'],['�л�Ӣ����','647145486'],['����','718659370'],['���','864602994'],['��Ӣ','1052654880']]####����������Ϣ�����ƺ͹ؼ���ID
for i in appList:
	c += 1
	name = i[0]
	ids = i[1]
	r = requests.get("http://aso100.com/app/keyword/appid/%s/country/cn"%(ids),headers=headers)
	html =  r.content#decode("utf-8")
	kwsData = eval(re.findall(r'<script>var tableData = (.*?)</script>',html)[0])
	for i in kwsData:
		kws = i[0].decode("unicode-escape")
		index = re.sub('#.*','',i[1])
		rank = i[2]
		comp = i[3]
		print kws,index,rank,comp
		f.write("%s\t%s\t%s\t%s\n"%(kws,index,rank,comp))
		f.flush()
print '�ؼ��������Ѿ����浽�ļ���APP������������-%s.txt'%(today)
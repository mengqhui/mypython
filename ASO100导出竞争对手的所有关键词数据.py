#!/usr/local/bin/python
# -*- coding:utf-8 -*-
######ASO100导出竞争对手的所有关键词数据
######作者：方法
######博客：http://seofangfa.com
######时间：2016-10-13

import re
import os
import json
import time,datetime
import requests
import sys
reload(sys)
from lxml import etree
sys.setdefaultencoding('utf-8')
import codecs	#为了生成gbk编码的文件
today = datetime.date.today()


headers = {

	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'AlexaToolbar-ALX_NS_PH':'AlexaToolbar/alx-4.0',
	'Cache-Control':'no-cache',
	'Cookie':'',###########替换成自己的cookie信息
	'DNT':'1',
	'Host':'aso100.com',
	'Pragma':'no-cache',
	'Proxy-Connection':'keep-alive',
	'Referer':'http://aso100.com/search?search=51job',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	}

f = open(unicode('APP所有排名导出-%s.txt'%(today),'utf-8'),'w')
c =0 
appList = [['智联招聘','488033535'],['58同城','480079300'],['前程无忧','415443644'],['猎聘','540996859'],['拉勾','1021464186'],['boss直聘','887314963'],['中华英才网','647145486'],['脉脉','718659370'],['大街','864602994'],['领英','1052654880']]####竞争对手信息，名称和关键词ID
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
print '关键词数据已经保存到文件：APP所有排名导出-%s.txt'%(today)

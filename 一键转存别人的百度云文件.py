#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#Date:2016.8.17
#Author:Fangfa@seofangfa.com
#���ã�һ��ת����˵İٶ����ļ�

import requests,time,random,json,StringIO,datetime,re,threading,urllib,Queue
import os
import codecs	#Ϊ������gbk������ļ�
today = datetime.date.today()
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')


########�����Ǳ����5�������������ȡ�����Ժ������ϸ�Ľ̳̣�������д�����Ժ�ֱ�����г���ͺ���

bduss = ''####��ϸ�����µײ���ͼ����chrome����¼�ʺţ���F12�򿪿����߹��ߣ��л���network��һ����̬�����ַ����RequestHeaders����Cookie
stoken = ''####ͬ��
bdstoken = ''####ͬ��
uk = ''####��Ҫת����˵�uk����https://yun.baidu.com/share/home?uk=154024822��uk��Ϊ154024822
path = '/'####���ڴ����ĸ��ļ������Ҫ��ǰ�������ļ��У�Ҳ����д/ȫ�������ڸ�Ŀ¼

##############������header

headers = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'BDUSS=%s;STOKEN=%s;'%(bduss,stoken),
'DNT':'1',
'Host':'yun.baidu.com',
'Pragma':'no-cache',
'Referer':'https://yun.baidu.com/share/home',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
	}

###����ת��ĺ���
def zhuanCun(filelist,path,shareid,uk,bdstoken,headers):	
	payload={
	'filelist':filelist,
	'path':path,
	}
	r = requests.post("https://yun.baidu.com/share/transfer?shareid=%s&from=%s&bdstoken=%s&channel=chunlei&web=1&app_id=250528&logid=MTQ3MTQxNDgyNTU0NjAuNzEzODExNTI5MjY3NjMx&clienttype=0"%(shareid,uk,bdstoken),headers=headers,data=payload)
	html = r.content
	# print html
	if '"errno":12' in html:
		print "file exit!"
	elif '"errno":0' in html:
		print "success!"
	else:
		print html
		

########��ȡ�������������ҳ��
payload = {
't':'1471410879156',
'category':'0',
'auth_type':'1',
'request_location':'share_home',
'start':'0',
'limit':'60',
'query_uk':uk,
'channel':'chunlei',
'clienttype':'0',
'web':'1',
}
r = requests.get("https://yun.baidu.com/pcloud/feed/getsharelist",headers=headers,params=payload)
html = r.content
# print html
jsons = json.loads(html)
# print type(jsons)
totalCount =  jsons['total_count']
print "�ܹ���%s��������ļ�"%(totalCount)
page = int(math.ceil(totalCount/60.0))
print "����%sҳ"%(page)
for c in range(page):	
	start = 60*c
	payload = {
	't':'1471410879156',
	'category':'0',
	'auth_type':'1',
	'request_location':'share_home',
	'start':start,
	'limit':'60',
	'query_uk':uk,
	'channel':'chunlei',
	'clienttype':'0',
	'web':'1',
	}
	r = requests.get("https://yun.baidu.com/pcloud/feed/getsharelist",headers=headers,params=payload)
	html = r.content
	jsons = json.loads(html)
	count = len(jsons['records'])
	print "����ת���%sҳ���ܹ���%s��"%(c+1,count)
	allFile = []
	for i in range(count):
		shareid = jsons['records'][i]['shareid']
		filelist = '["%s"]'%(urllib.unquote(str(jsons['records'][i]['filelist'][0]['path'])).decode('utf-8').encode('utf8'))
		allFile.append("%s,%s"%(shareid,filelist))	
		print i,shareid,filelist
		zhuanCun(filelist,path,shareid,uk,bdstoken,headers)
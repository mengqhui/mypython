# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import csv
import socket

def IPspider(numpage):
	csvfile = file('ipy.csv', 'wb')
	writer = csv.writer(csvfile)
	url='http://www.xicidaili.com/nn/'
	user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'
	headers={'User-agent':user_agent}
	for num in xrange(1,numpage+1):
		ipurl=url+str(num)
		print 'Now downloading the '+str(num*100)+' ips'
		request=urllib2.Request(ipurl,headers=headers)
		content=urllib2.urlopen(request).read()
		bs=BeautifulSoup(content,'html.parser')
		res=bs.find_all('tr')
		for item in res:
			try:
				temp=[]
				tds=item.find_all('td')
				'''
				temp.append(tds[1].text.encode('utf-8'))
				temp.append(tds[2].text.encode('utf-8'))
				'''
				temp.append(IPpool(tds[1].text.encode('utf-8'),tds[2].text.encode('utf-8')))
				writer.writerow(temp)
			except IndexError:
					pass
def IPpool(ip,port):
	socket.setdefaulttimeout(2)
	#reader=csv.reader(open('ips.csv'))
	IPpool=[]
	#for row in reader:
	proxy=ip+':'+port
	proxy_handler=urllib2.ProxyHandler({"http":proxy})
	opener=urllib2.build_opener(proxy_handler)
	urllib2.install_opener(opener)
	try:
		html=urllib2.urlopen('http://www.baidu.com')
		IPpool.append(ip)
		IPpool.append(port)
	except Exception,e:
		print e
		#continue
	return IPpool

#假设爬取前十页所有的IP和端口
IPspider(10)

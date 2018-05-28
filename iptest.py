# -*- coding: utf-8 -*-

import urllib2
import threading
import socket
import csv
'''
inFile = open('ips.csv', 'r')
outFile = open('available.txt', 'w')
url = 'http://www.baidu.com'
lock = threading.Lock()


def test():
	lock.acquire()
	line = inFile.readline().strip()
	lock.release()
	# if len(line) == 0: break
	protocol, proxy = line.split('=')
	#cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="
	try:
		proxy_support = urllib2.ProxyHandler({protocol.lower():'://'.join(line.split('='))})
		opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
		urllib2.install_opener(opener)
		request = urllib2.Request(url)
		#request.add_header("cookie",cookie)
		content = urllib2.urlopen(request,timeout=4).read()
		if len(content) >= 1000:
			lock.acquire()
			print 'add proxy', proxy
			outFile.write('\"%s\",\n' %proxy)
			lock.release()
		else:
			print '出现验证码或IP被封杀'
	except Exception, error:
		print error
all_thread = []
for i in range(500):
	t = threading.Thread(target=test)
	all_thread.append(t)
	t.start()

for t in all_thread:
	t.join()

inFile.close()
outFile.close()
'''
def IPpool():
	socket.setdefaulttimeout(2)
	reader=csv.reader(open('ips.csv'))
	IPpool=[]
	for row in reader:
		proxy=row[0]+':'+row[1]
		proxy_handler=urllib2.ProxyHandler({"http":proxy})
		opener=urllib2.build_opener(proxy_handler)
		urllib2.install_opener(opener)
		try:
			html=urllib2.urlopen('http://www.baidu.com')
			IPpool.append([row[0],row[1]])
		except Exception,e:
			continue
	return IPpool

print(IPpool())
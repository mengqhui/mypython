#!/usr/local/bin/python
#coding:utf8
# 2015-6-26 DaoXin
import pycurl, json, MySQLdb
import StringIO
import urllib, urllib2
from random import choice
import sys 
reload(sys)
sys.setdefaultencoding('utf8')
#useragent 列表，大家可以自行去收集。不过在本例中似乎不需要这个
AGENTS = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
            "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-CN) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; zh-CN) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; zh-CN) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
]

UserAgent = choice(AGENTS)


#如果需要把挖出来的关键词保存到数据库，需要配置数据库相关信息
class ConnDb():
    global host, user, passwd, db
    host = '111.111.111.111' #数据库IP
    user = 'python' #数据库用户名
    passwd = 'pass' #数据库密码
    db = 'dbnamelllllll' # 数据库名
    def connDb(self):
        global cur
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=3306, charset = 'utf8')
        cur = conn.cursor()
        return cur

# 这个curl方法是从zero那里扒过来的。http://www.seoqx.com/post/341
def curl(url, debug=False, **kwargs):
    while 1:
        try:
            s = StringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, url)
            c.setopt(pycurl.REFERER, url)
            c.setopt(pycurl.FOLLOWLOCATION, True)
            c.setopt(pycurl.TIMEOUT, 60)
            c.setopt(pycurl.ENCODING, 'gzip')
            c.setopt(pycurl.USERAGENT, UserAgent)
            c.setopt(pycurl.NOSIGNAL, True)
            c.setopt(pycurl.WRITEFUNCTION, s.write)
            for k, v in kwargs.iteritems():
                    c.setopt(vars(pycurl)[k], v)
            c.perform()
            c.close()
            return s.getvalue()
        except:
            if debug:
            	raise
            continue

command = int(raw_input("请选择导出形式；1：导出为txt，2：导入道数据库: "))

if command == 1:
	FileWrite = open("output.txt", 'w')
	for line in open('sourceword.txt'):
		kw = str(line)
		jsons = curl('http://honeyimg.bdimg.com/recomword/recomWordCache_findRecomWord.htm?area_id=&word=' + urllib.quote_plus(kw))
		d = json.loads(jsons)
		try:
			dlist = d['data']['list']
			for item in dlist:
				indexs = item['total']
				keywords = item['word'].encode('utf-8')
				outstr = str(indexs) + ',' + str(keywords) + '\n'
				FileWrite.write(outstr)
		except TypeError, e:
			print 'TypeError, Pass', e
			continue
	print 'done to txt'
elif command == 2:
	conndb = ConnDb()
	conndb.connDb()
	for line in open('sourceword.txt'):
		kw = str(line)
		jsons = curl('http://honeyimg.bdimg.com/recomword/recomWordCache_findRecomWord.htm?area_id=&word=' + urllib.quote_plus(kw))
		d = json.loads(jsons)
		try:
			dlist = d['data']['list']
			for item in dlist:
				indexs = item['total']
				#keywords = unicode(item['word'], 'utf-8')
				keywords = item['word'].encode("utf-8")
				sql = "insert into shangqing_keyword (id, total, keyword) values (null, '%s', '%s')"
				try:
					cur.execute(sql % (indexs, keywords))
				except MySQLdb.Error, e:
					print 'MySql error', e
					continue
		except TypeError, e:
			print 'TypeError, Pass' , e
			continue
	print 'done to mysql'
else:
	print '只有两种导出方式，请输入1或者2'

import urllib2,re
for key in open('key.txt'): 
	do = "http://suggest.taobao.com/sug?code=utf-8&q=%s" % key.rstrip()
	_re = re.findall('\[\"(.*?)\",\".*?\"\]',urllib2.urlopen(do).read())
	for i in _re :
		print i
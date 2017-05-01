#coding=utf-8
import re
def tokenize(text, match=re.compile("([idel])|(/d+):|(-?/d+)").match):
	i = 0
	while i < len(text):
		m = match(text, i)
		s = m.group(m.lastindex)
		i = m.end()
		if m.lastindex == 2:
			yield "s"
			yield text[i:i+int(s)]
			i = i + int(s)
		else:
			yield s
def decode_item(next, token):
	if token == "i":
		# integer: "i" value "e"
		data = int(next())
		if next() != "e":
			raise ValueError
	elif token == "s":
		# string: "s" value (virtual tokens)
		data = next()
	elif token == "l" or token == "d":
		# Container: "l" (or "d") values "e"
		data = []
		tok = next()
		while tok != "e":
			data.append(decode_item(next, tok))
			tok = next()
		if token == "d":
			data = dict(zip(data[0::2], data[1::2]))
	else:
		raise ValueError
	return data
def decode(text):
	try:
		src = tokenize(text)
		data = decode_item(src.next, src.next())
		for token in src: # look for more tokens
			raise SyntaxError("trailing junk")
	except (AttributeError, ValueError, StopIteration):
		raise SyntaxError("syntax error")
	return data
if __name__ == "__main__":
#需要读取的文件名称放到这里
	data = open(u"LJZ4JD8.torrent", "rb").read()
	torrent = decode(data)
	myfile = file("testit.txt", 'w')
	a = u'文件名称'.encode('gbk')
	b = u'文件大小'.encode('gbk')
	print "%s /t %s /n" % (a,b)
	for file in torrent["info"]["files"]:
		print "%s /t %d Mb " % ("/".join(file["path"]), file["length"]/1024/1024)
		print "-----------------------------------------------------------------"

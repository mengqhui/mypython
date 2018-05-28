# -*-coding:utf-8-*-
# coding:utf-8

import sys
import time
import urllib2

from bs4 import BeautifulSoup

from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')  # 设置编码

name = ""
scores = ""
baidu = ""
google = ""
vtype = ""
numbers = ""
userss = ""
hherf = ""

fo = open('table.txt', 'w')
# //*[@id="container"]/table
driver = webdriver.PhantomJS()

for i in range(28):
    print(i)
    urlbase = "http://hao.huangye88.com/pn"
    url = urlbase+str(i)
    '''
	try:  
		page = urllib2.urlopen(url, timeout = 1)  
	except urllib2.URLError, e:  
		raise MyException("There was an error: %r" % e)  
	'''
    #req = urllib2.Request(url)
    #page = urllib2.urlopen(req)
    #page = urllib2.urlopen(url, timeout = 1)
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html5lib')
    tabb = soup.find("table", {"class": "sod"}).find("tbody")
    #rows = tabb.find_all('tr')
    fo.write(str(tabb))
    # time.sleep(10)
fo.close()

for row in rows:
    cells = row.findAll("td")
    data = []
    if len(cells) == 8:
        name = cells[0].find("a").string
        scores = cells[1].find("span", attrs={'class': "score"}).string
        baidu = cells[2].get_text()
        google = cells[3].find(text=True)
        vtype = cells[4].find(text=True)
        numbers = cells[5].find(text=True)
        userss = cells[6].find(text=True)
        hherf = cells[7].a.get('href')
    data = [name, scores, baidu, google, vtype, numbers, userss, hherf]
    for da in data:
        fo.write(da.decode('utf-8')+'\t')
    # fo.writelines(data)
    fo.write('\n')


driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")
# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

# 用js方法输入日期
js_value = 'document.getElementById("train_date").value="2016-12-25"'
driver.execute_script(js_value)

# # 清空文本后输入值
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2016-12-25")


'''
网站名称
网站评分
百度收录速度
谷歌收录速度
类型
可发数量
用户印象
快速发布
'''

cells = row.findAll("td")
if len(cells) == 8:
    name = cells[0].find("a").string
    scores = cells[1].find("span", attrs={'class': "score"}).string
    baidu = cells[3].find(text=True)
    google = cells[4].find(text=True)
    vtype = cells[5].find(text=True)
    numbers = cells[6].find(text=True)
    userss = cells[7].find(text=True)
    hherf = cells[7].a.get('href')


rows = tabb.find_all('tr')
for row in rows:
    cols = row.find_all('td')

# -*- coding: utf-8 -*-
import os
import random
import time

import requests

url = [
    # 'http://page2.yunfile.com/verifyimg/getPcv.html',
    'http://page1.dfpan.com/verifyimg/getPcv.html',
    'http://page2.dfpan.com/verifyimg/getPcv.html',
    'http://page3.dfpan.com/verifyimg/getPcv.html',
    'http://page4.dfpan.com/verifyimg/getPcv.html'

]
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'
}
UserAgent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible;MSIE6.0;WindowsNT5.1)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;360SE)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
    "Mozilla/4.0 (compatible;MSIE7.0;WindowsNT6.0)",
    "Mozilla/4.0 (compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/5.0 (Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0 (Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0 (WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
    "Opera/9.80 (Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "Opera/9.80 (WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"
]


def getPcv(i):
    time.sleep(1)
    try:
        r = requests.get(random.choice(url), headers=header)
        i = '%03d' % i
        if i.endswith('0'):
            print(s, i, time.ctime())
        jpgname = str(i)+'.jpg'
        with open(jpgname, 'wb') as code:
            code.write(r.content)
        code.close()
    except Exception, e:
        print i, Exception, ":", e
    finally:
        return


for j in range(77, 80):
    time.sleep(3)
    s = "%03d" % j
    # print(s)
    os.mkdir(str(s))
    os.chdir(str(s))
    for i in range(1000):
        getPcv(i)
    os.chdir('../')

import urllib.request
import urllib.parse
import base64
import time
from PIL import Image
import os
from random import choice

url = "https://ai.baidu.com/aidemo"

headers = {
    "Host": " ai.baidu.com",
    "Origin": " https://ai.baidu.com",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": "",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": " https://ai.baidu.com/tech/ocr/general",
    "Cookie": " BAIDUID=5132C9BFC8AF76FF01DB7EE7A5020B4E:FG=1;\
 BIDUPSID=5132C9BFC8AF76FF01DB7EE7A5020B4E; PSTM=1524625812;\
 FP_UID=1bb184fbb0534f47b18fcf3dee60aea7;\
 BDRCVFR[4Zjqyl1bxbt]=mk3SLVN4HKm;\
 BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm;\
 BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm;\
 pgv_pvi=5921132544; pgv_si=s6378953728; docVersion=0;\
 seccode=5d0dd163973957973e95b1c182c88715;\
 Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525050283,1525054553,1525069086,1525136655;\
 Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525137559;\
 PSINO=2; H_PS_PSSID=1430_21108_26106"
}

UserAgent = ["Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
             "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
             "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
             "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
             "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
             "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
             "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
             "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
             "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
             "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
             "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"
             "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
             ]

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return base64.b64encode(fp.read())


def merge_pic(n):
    """ 读取图片 """
    j = 4
    toImage = Image.new('RGBA', (80, j*25))
    jpgs = []
    for (i, ii) in zip(range(j*n, j*(n+1)), range(j)):
        jpg_n = str(i) + '.jpg'

        jpgs.append(jpg_n)
        fimage = Image.open(jpg_n)

        loc = (0, ii*25)
        # print(loc,jpg_n)
        toImage.paste(fimage, loc)

    toImage.save('tmp.png')

    return get_file_content('tmp.png'), jpgs


for n in range(0, 250):
    time.sleep((n % 3+1)*2)
    image_b, image_l = merge_pic(n)

    data = {'type': 'commontext',
            'image': '',
            'image_url': ''}

    img = u'data:image/png;base64,' + image_b.decode(encoding='UTF8')

    data['image'] = img

    datas = urllib.parse.urlencode(data).encode(encoding='UTF8')

    headers["User-Agent"] = choice(UserAgent)

    request = urllib.request.Request(url=url, data=datas, headers=headers)
    response = urllib.request.urlopen(request)

    res_basicAccurate = response.read().decode(encoding='UTF8')
    res_basicAccurate = eval(res_basicAccurate)

    if 'words_result_num' in res_basicAccurate['data'] and res_basicAccurate['data']['words_result_num'] is 4:
        words_result = res_basicAccurate['data']['words_result']
        words = [n['words'] for n in words_result]

        for (o, n) in zip(image_l, words):
            print(o, n)
            try:
                os.rename(o, '[' + n + '.jpg')
            except:
                continue

    else:
        print(res_basicAccurate)
        continue

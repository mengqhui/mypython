import base64
import glob
import os
import sys
import time
from io import BytesIO
from random import choice
from urllib import parse, request

from PIL import Image
from tqdm import tqdm

tqdm.monitor_interval = 0
url = "https://ai.baidu.com/aidemo"

headers = {
    "Host": " ai.baidu.com",
    "Origin": " https://ai.baidu.com",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": "",
    "Cookie": " BAIDUID=5132C9BFC8AF76FF01DB7EE7A5020B4E:FG=1;\
 BIDUPSID=5132C9BFC8AF76FF01DB7EE7A5020B4E; PSTM=1524625812; FP_UID=1bb184fbb0534f47b18fcf3dee60aea7;\
 BDRCVFR[4Zjqyl1bxbt]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm;\
 pgv_pvi=5921132544; pgv_si=s6378953728; docVersion=0; seccode=5d0dd163973957973e95b1c182c88715;\
 Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525050283,1525054553,1525069086,1525136655;\
 Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525137559; PSINO=2; H_PS_PSSID=1430_21108_26106",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": " https://ai.baidu.com/tech/ocr/general"
}

Cookie_s = ["BAIDUID=5132C9BFC8AF76FF01DB7EE7A5020B4E:FG=1; BIDUPSID=5132C9BFC8AF76FF01DB7EE7A5020B4E; PSTM=1524625812;\
 Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525217034,1525264277,1525417203,1525420900;\
 Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525420900; seccode=6d19f039ff135c519ce87b1100bab421",
            "BIDUPSID=2925CA383A0843DEBE7500E118AD525A; PSTM=1499133579; BAIDUID=F0FEFA901EC95A57FB5C75BBE1D36C78:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;\
 BDUSS=0RQWGRZbzFOR0gzakxoUkhlVlJsOW5rbE9VUjBUZXdEQjFoUn4wTVhyNEUtUkZiQVFBQUFBJCQAAAAAAAAAAAEAAADixeov1qez1rbIxO9kYXkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARs6loEbOpad;\
 docVersion=0; H_PS_PSSID=1469_21080_18560_22074; PSINO=2; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525258023,1525393787,1525421040; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525421040; seccode=7e9d19f9c4875f011d13eb8a4c61ca60",
            "BIDUPSID=4764453D5F826C68F67AD333B328F3C0; PSTM=1487382371;\
 BDUSS=EMtNzhOVk9hNDkwZnlHbEd-MFktUERPQjU4Q1lidFF0R2FmNWtDRFRjUmhqZ0ZaSVFBQUFBJCQAAAAAAAAAAAEAAADixeov1qez1rbIxO9kYXkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEB2lhhAdpYa;\
 BAIDUID=C1B207825E124A0C4B9268DF3DA17159:FG=1; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525170705;\
  H_PS_PSSID=1438_21115_22160; BDSFRCVID=45IsJeCCxG3AXbJAg-422qdpwktyEwBj-Gr93J; H_BDCLCKID_SF=tR-f_CP2tI_3fP36q4n_h-4ehmTXKR0sQ6TRQhcH0KLKEJv9WJ5jWRFOBUOi--jZ3Cke3Ct52fb1MRjVLt-a0jjX0Pbx-tbBJbRM0l5TtUJa8DnTDMRh-l4PMUbyKMnitIj9-pnKaMt0hC_xD5AhDTvM5pJfeJJy5jn30RjeHJO_bPQFyJbkbfJBDGjj--rHJGQga4btbpvaoqTNDRCWj-47yajKB4TQQ5bWbUJ13-jRexPR0popQT8rKtFOK5OibCujVxQ4ab3vOIJzXpO1544reGLs54FXKD600PK8Kb7VbI-GyJbkbftd2-te3lvaWe6MsC--ttjfq-3c5brp5UDqqtJHq6JZfD7H3KCbtCKaMU5; PSINO=2; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm; BDRCVFR[AuGWY-B7ujm]=9xWipS8B-FspA7EnHc1QhPEUf; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1525421112; seccode=483d71535cc329ddd7e753e9775f3e31"
            ]
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


def Respawn():
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(1)
    print("Respawning")
    os.execvp(executable, args)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return base64.b64encode(fp.read())


def merge_pic(n):
    # 读取图片
    # 若img.save()报错 cannot write mode RGBA as JPEG
    # 则img = Image.open(image_path).convert('RGB')

    toImage = Image.new('RGB', (80, j*25))
    for (jpg_n, ii) in zip(n, range(j)):
        fimage = Image.open(jpg_n)
        loc = (0, ii*25)
        toImage.paste(fimage, loc)

    output_buffer = BytesIO()
    toImage.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


l = glob.glob('*/*.jpg')
num = len(l)
j = 4
for nu in tqdm(range(0, num, j)):
    if nu % 960 is 0:
        headers['Cookie'] = choice(Cookie_s)

    ll = l[nu:nu+j]
    time.sleep((nu % 3+1)*1)
    image_b = merge_pic(ll)

    data = {'type': 'commontext',
            'image': '',
            'image_url': ''}

    img = 'data:image/jpeg;base64,' + image_b.decode(encoding='UTF8')
    data['image'] = img
    datas = parse.urlencode(data).encode(encoding='UTF8')

    headers["User-Agent"] = choice(UserAgent)
    req = request.Request(url=url, data=datas, headers=headers)
    resp = request.urlopen(req)

    res_bA = resp.read().decode(encoding='UTF8')
    res_bA = eval(res_bA)

    if res_bA['errno'] is 0 and res_bA['data']['words_result_num'] is 4:
        words_result = res_bA['data']['words_result']

        for (o, n) in zip(ll, words_result):
            if n['words'].isdigit() and len(n['words']) is 4:

                for g in glob.glob('D:\\个人\\验证码\\002\\*'):
                    new = g + '\\' + n['words'] + '.jpg'
                    if os.path.exists(new) is False:
                        try:
                            os.rename(o, new)
                            print(o, new)
                        except WindowsError as e:
                            print('new {}'.format(e))
                            continue
                    else:
                        break

                if os.path.exists(o) is True:
                    try:
                        os.rename(o, '037/040/' + n['words'] +
                                  '-' + str(time.time()) + '.jpg')
                    except WindowsError as e:
                        print('finally:{}'.format(e))
                        continue

    elif res_bA['errno'] is 102:
        print('请求Demo过于频繁！！sleeping 300s !!')
        time.sleep(300)
        Respawn()

    else:
        print(res_bA['msg'])

#妹子图（http://www.mzitu.com）爬取特定图集的 Python 实现
import requests
from bs4 import BeautifulSoup
import os
import time
 
 
class Spider:
    def __init__(self, base_url):
        self.base_url = base_url
 
    def run(self):
        for i in range(1, 10000):
            url = '{}/{}'.format(base_url, i)
            html = self.request(url)
            if html:
                self.parse_html(html, url)
                time.sleep(1)
            else:
                time.sleep(0.5)
 
    def parse_html(self, html, href):
        title = BeautifulSoup(html.text, 'lxml').find('h2', class_='main-title').text
        print('开始保存：{}'.format(title))
        path = str(title)
        self.mkdir(path)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].text
        for page in range(1, int(max_span) + 1):
            if page == 1:
                page_url = href
            else:
                page_url = '{}/{}'.format(href, str(page))
            self.parse_img(page_url, img_name=page)
 
    def parse_img(self, page_url, img_name):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save_img(img_url, img_name)
 
    def save_img(self, img_url, img_name):
        img = self.request(img_url)
        with open('{}.jpg'.format(img_name), 'ab') as f:
            f.write(img.content)
 
    def request(self, url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64)"
                          " AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        }
        content = requests.get(url, headers=headers, allow_redirects=False)
        if content.status_code != 200:
            return False
        else:
            return content
 
    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            print(u'创建', path, u'文件夹')
            os.makedirs(os.path.join("D:\MZITU", path))
            os.chdir(os.path.join("D:\mzitu", path))  # 切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了')
            return False
 
if __name__ == '__main__':
    base_url = 'http://www.mzitu.com'
    spider = Spider(base_url)
    spider.run()
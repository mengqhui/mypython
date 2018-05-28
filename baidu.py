import os

from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
from selenium.webdriver import FirefoxOptions as FFO
from selenium.webdriver.chrome import options

profile_dir = os.getenv('localappdata') + '\\Google\\Chrome\\User Data'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度

# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#chrome_options.add_argument('--headless')

chrome_options.add_argument("user-data-dir=" + profile_dir)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
url = 'https://wenku.baidu.com/task/browse/daily'
driver.get(url)
driver.find_element_by_css_selector(
    '#signin > div.bd > div.clearfix.new-sidebar > span').click()
"""
#kw
#su
"""

[
    'http://xueshu.baidu.com/u/paperhelp',
    'http://xueshu.baidu.com/usercenter/?tab=collect',
    'http://xueshu.baidu.com/usercenter',  ##wrapper > p > span.typeitem.sel
]
driver.get('http://xueshu.baidu.com/usercenter')
driver.find_element_by_css_selector('#wrapper > p > span.typeitem.sel').click()

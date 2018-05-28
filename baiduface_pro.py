# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import unittest, time, re, os, json

driver = webdriver.Firefox()
driver.implicitly_wait(30)
#driver.get("http://ai.baidu.com/tech/face/detect")
time.sleep(3)
for i in range(19):
	actions = ActionChains(driver)
	actions.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

handles = driver.window_handles
for newhandle in handles:
	driver.switch_to_window(newhandle)
    driver.get("http://ai.baidu.com/tech/face/detect")
    
with open('E:\picture.txt','r') as pic:
    plines = pic.readlines()
    
    batch = len(handles)
    xy=zip(handles,plines)
    
for x,y in xy:
    driver.switch_to_window(x)
    fp = y.strip().decode('u8')
    print(fp)
    driver.find_element_by_css_selector("input[type=\"file\"]").clear()
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(fp)
    time.sleep(5)
    
    try:  
        is_disappeared = WebDriverWait(driver, 5, 0.5).until(text_to_be_present_in_element_value(driver.find_element_by_xpath('//*[@id="demo-json"]/p'),'success'))
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="demo-json"]/p'))
        
"""
POST /aidemo HTTP/1.1
Host: ai.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://ai.baidu.com/tech/face/detect
Content-Length: 30272
Cookie: BAIDUID=F31E6AE401BEEF6E89827D6B967DE1D3:FG=1; seccode=d153f7b8bcbeab02ffdb4c7223330996; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185175; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185409
Connection: keep-alive

POST /aidemo HTTP/1.1
Host: ai.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://ai.baidu.com/tech/face/detect
Content-Length: 30034
Cookie: BAIDUID=F31E6AE401BEEF6E89827D6B967DE1D3:FG=1; seccode=d153f7b8bcbeab02ffdb4c7223330996; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185175; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185409
Connection: keep-alive

POST /aidemo HTTP/1.1
Host: ai.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://ai.baidu.com/tech/face/detect
Content-Length: 142
Cookie: BAIDUID=F31E6AE401BEEF6E89827D6B967DE1D3:FG=1; seccode=d153f7b8bcbeab02ffdb4c7223330996; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185175; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1505185409
Connection: keep-alive
"""
"""
<div class="canvas-container loading"><canvas width="592" height="400" data-scale="0.9932432432432432" style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%) scale(0.993243);">您的浏览器暂时不支持canvas，请选用现代浏览器！</canvas></div>
//*[@id="demo-json"]/p
html body.ai-platform div.ai-content div#tech-demo.tech-section.tech-demo div.ai-container div.demo-container.clear-float div.clear-float div.data-view-container div#demo-json.data-view
html body.ai-platform div.ai-content div#tech-demo.tech-section.tech-demo div.ai-container div.demo-container.clear-float div.clear-float div.data-view-container div#demo-json.data-view p
#demo-json > p
//*[@id="demo-json"]

#result-gallery > ul
/html/body/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]
html body.ai-platform div.ai-content div#tech-demo.tech-section.tech-demo div.ai-container div.demo-container.clear-float div.clear-float div.data-view-container div#demo-result.data-view div#result-gallery ul.gallery-container li.active
//*[@id="result-gallery"]/ul

#modal-1505181570291 > section:nth-child(2) > div:nth-child(1)
html body.ai-platform.modal-show div#modal-1505181570291.ai-modal.alert section.modal-content div
html body.ai-platform div.ai-content div#tech-demo.tech-section.tech-demo div.ai-container div.demo-container.clear-float div.clear-float div.data-view-container div#demo-result.data-view div.canvas-container.has-result

#type=face
#image_url
"""
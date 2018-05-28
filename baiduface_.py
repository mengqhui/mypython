# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time, re, os, json, logging
logging.basicConfig(level=logging.INFO, filename='log_pic.txt',
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://ai.baidu.com/tech/face/detect")
os.system('pause')

with open('D:\pic.txt','r') as pic:
    plines = pic.readlines()
    batch = 20
    x = [plines[k:k+batch] for k,j in enumerate(plines) if k%batch is 0]
tt = time.time()
for ps in x:
    for fp in ps:
        fp = fp.strip()#.decode('u8')
        print(fp)
        #driver.find_element_by_css_selector("input[type=\"file\"]").clear()
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(fp)
        time.sleep(0.5)
        try:  
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(\
                        (By.XPATH, '//*[@id="demo-json"]/p'),u'success'))
        except Exception as e:
            print("异常：", e)

        att = driver.find_element_by_xpath('//*[@id="demo-json"]/p').text
        if "location" in att:
            with open(os.path.splitext(fp)[0]+'.json', 'a') as jsw:
                logging.info(u"共费时：{}(s) {}".format(time.time()-tt, fp))
                jsw.write(att)
    print(u"休息15秒!!")
    time.sleep(15)

driver.quit()
#os.system("shutdown /s")
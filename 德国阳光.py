# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"德国阳光蓄电池")
        driver.find_element_by_id("su").click()
        driver.find_element_by_link_text(u"德国阳光sonnenlicht官方授权总代理4007726580").click()
        driver.find_element_by_id("content_left").click()
        driver.get(self.base_url + "/s?wd=%E5%BE%B7%E5%9B%BD%E9%98%B3%E5%85%89%E8%93%84%E7%94%B5%E6%B1%A0&rsv_spt=1&rsv_iqid=0xe7966d72000722ba&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_t=dc84roNNumt1mB7OAD3E5da5Ub%2ByiI9ONtIw586IQsD7DNdDEiYYBP2hGRl9WvaSTS%2FT&rsv_sug2=0&inputT=3968&rsv_sug4=3969")
        driver.find_element_by_link_text(u"CSTK蓄电池全国总经销010-51266881").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

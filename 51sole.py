# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 51sole(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://user.51sole.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_51sole(self):
        driver = self.driver
		driver.get(self.base_url + "/user/commerces/createinfornew.aspx?bigtype=1&type=0")
		driver.find_element_by_id("txtCommerceTitle").clear()
		driver.find_element_by_id("txtCommerceTitle").send_keys(u"香港零售阳光蓄电池A512/25G5服务周到")
		driver.find_element_by_id("rbtnlsCommerceIndustry_2").click()
		driver.find_element_by_css_selector("div.showbtn > span").click()
		driver.find_element_by_id("Radio_60793").click()
		driver.find_element_by_id("Radio_60788").click()
		driver.find_element_by_id("rbtnlsCommerceIndustry_3").click()
		driver.find_element_by_id("txt_69778").clear()
		driver.find_element_by_id("txt_69778").send_keys("A412/65G6")
		driver.find_element_by_id("Radio_60950").click()
		driver.find_element_by_id("Radio_60961").click()
		driver.find_element_by_id("Radio_60963").click()
		driver.find_element_by_xpath("(//span[@onclick='ShowAllAttr(this)'])[5]").click()
		driver.find_element_by_id("Radio_333340").click()
		driver.find_element_by_id("Radio_333338").click()
		driver.find_element_by_id("pickongjian").click()
		driver.find_element_by_css_selector("img[alt=\"50a (4).jpg\"]").click()
		driver.find_element_by_id("insertOk").click()
		driver.find_element_by_id("txtBrand668").clear()
		driver.find_element_by_id("txtBrand668").send_keys(u"德国阳光")
		driver.find_element_by_id("txtCaseDetail").clear()
		driver.find_element_by_id("txtCaseDetail").send_keys(u"全包装")
		driver.find_element_by_id("txtProductSpec").clear()
		driver.find_element_by_id("txtProductSpec").send_keys("A412/65G6")
		driver.find_element_by_id("txtCommerceContent").clear()
		driver.find_element_by_id("txtCommerceContent").send_keys(u"2.未对供应商进行规范管理，一项不符合扣1分；\n(2) 聚类分析首先通过分析视频数据库中的数据，将具有相同特性的数据聚集在一起， 合理地划分记录，然后再确定每个数据对象所在的类别。聚类分析不同于分类，将 数据分成几类是事先并不知道的。聚类算法一般分为基于概率的聚类算法和基于距 离的聚类算法。视频对象的聚类在视频结构分析中具有重要的作用，例如，利用聚 类算法可以将特征相似的镜头聚集成更高层的结构单元一一场景。\n170\n　　b)	拥有全国百万家企业基础数据库\n10\n①将K1扳到ON。\n有限元模型\n420Ah\n12V\n        （6）控制电池放电保护电压。36  V电池组放电保护电压为31.5或42V(48V电池组)。\nBASF Battery Materials - Ovonic\n4\n2.03\n18621631419\n15110208454\nwww.sonnenlicht029.com\nwww.upszhijia.com\n　　UPS电源由内部风扇提供强制风冷，通过机柜下部风栅进入UPS内部，并通过后部风扇排出。在设计UPS机房的通风冷却系统时请注意各种UPS的功耗和通风量数据。")
		driver.find_element_by_id("btn_newCommerce").click()
    
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

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Redocn(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://sucai.redocn.com"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_redocn(self):
		numbers="3788358"
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("keyword").click()
		driver.find_element_by_id("keyword").click()
		driver.find_element_by_id("keyword").clear()
		driver.find_element_by_id("keyword").send_keys("3788358")
		driver.find_element_by_css_selector("input.search_btn").click()
		canshu=driver.find_element_by_css_selector("div.good_canshu")
		print(canshu)
		
	def save_redocn(self):
		driver = self.driver
		#body > div.g-doc > div.content_good > div.good_right > div.good_canshu
		canshu=driver.find_element_by_css_selector("div.good_canshu")
		print(canshu)
	
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

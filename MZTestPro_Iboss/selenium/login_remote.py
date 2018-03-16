# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class login_remote(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.16.0.25:8011/")
        self.selenium.start()
    
    def test_login_remote(self):
        sel = self.selenium
        sel.open("/login.nk")
        sel.type("//input[@id='id_name']", "4222787")
        sel.type("//input[@id='id_password']", "0359422400")
        sel.click("//button[@type='submit']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

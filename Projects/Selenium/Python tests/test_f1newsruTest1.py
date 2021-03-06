# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestF1newsruTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_f1newsruTest1(self):
    # Test name: f1news.ru - Test1
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.f1news.ru/")
    # 2 | setWindowSize | 1500x960 | 
    self.driver.set_window_size(1500, 960)
    # 3 | runScript | window.scrollTo(0,2) | 
    self.driver.execute_script("window.scrollTo(0,2)")
    # 4 | click | linkText=В Honda не считают, что дверь в Формулу 1 закрыта | 
    self.driver.find_element(By.LINK_TEXT, "В Honda не считают, что дверь в Формулу 1 закрыта").click()
    # 5 | runScript | window.scrollTo(0,218.5) | 
    self.driver.execute_script("window.scrollTo(0,218.5)")
    # 6 | runScript | window.scrollTo(0,1431.5) | 
    self.driver.execute_script("window.scrollTo(0,1431.5)")
    # 7 | runScript | window.scrollTo(0,1880) | 
    self.driver.execute_script("window.scrollTo(0,1880)")
    # 8 | click | css=.header_top | 
    self.driver.find_element(By.CSS_SELECTOR, ".header_top").click()
    # 9 | click | css=.b-logo__img | 
    self.driver.find_element(By.CSS_SELECTOR, ".b-logo__img").click()
    # 10 | mouseOver | linkText=В Honda не считают, что дверь в Формулу 1 закрыта | 
    element = self.driver.find_element(By.LINK_TEXT, "В Honda не считают, что дверь в Формулу 1 закрыта")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | linkText=В Honda не считают, что дверь в Формулу 1 закрыта | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 12 | click | linkText=Дарувала вернётся за руль McLaren MCL35M в Портимао | 
    self.driver.find_element(By.LINK_TEXT, "Дарувала вернётся за руль McLaren MCL35M в Портимао").click()
    # 13 | runScript | window.scrollTo(0,400) | 
    self.driver.execute_script("window.scrollTo(0,400)")
    # 14 | close |  | 
    self.driver.close()
  

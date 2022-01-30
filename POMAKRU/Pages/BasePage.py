import webbrowser
import click
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is parent of all the pages"""

"""It contains all the generic methods and utilities for all the pages"""


class BasePage:
    """constructor"""
    def __init__(self,driver):
        self.driver=driver


    """method for locating for click elements"""
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()


    """method for locating  elements for sending key"""  
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

   
   """method for locating for  elements"""
    def is_visible(self,by_locator):
       element= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)) 
       return element

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(params=["chrome"], scope='class')
def init__driver(request):
    s=Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if request.param=="chrome":
       web_driver = webdriver.Chrome(options=options,service=s)
    if request.param=="firefox":
       web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if request.param=="opera":
       web_driver = webdriver.Opera(executable_path=OperaDriverManager().install())   
    request.cls.driver=web_driver
    #web_driver.implicitly_wait(15)

    """ TEARDOWN"""
    yield
    web_driver.quit() 
import time
from POMAKRU.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from POMAKRU.Config.config import TestData
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YopmailPage(BasePage):
    """CREATING LOCATORS OF YOPMAIL"""

    YOP_EMAIL_FIELD=(By.CLASS_NAME,'ycptinput')
    YOP_SEND_BTN=(By.XPATH,'//*[@id="refreshbut"]/button/i')
    YOP_FRAME=(By.ID,'ifmail')
    YOP_MAGICLINK_BTN=(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
    YOP_MAGIC_LINK=(By.LINK_TEXT,'Click here')
    SIGNUP_LINK = (By.LINK_TEXT,'Continue Signup')
    
    """constructor"""
    def __init__(self,driver):
        self.driver=driver


    def Yopmail(self,email):
        """ RUNNING SCRIPT TO THE NEW WINDOW"""
        self.driver.execute_script("window.open()")

        """ ASSIGNING INDEX 1 TO YOPMAIL WINDOW"""
        self.driver.switch_to.window(self.driver.window_handles[1])    
        self.driver.get(TestData.YOPMAIL_URL)
        self.do_send_keys(self.YOP_EMAIL_FIELD,email)
        self.do_click(self.YOP_SEND_BTN)
        self.driver.switch_to.frame(self.is_visible(self.YOP_FRAME))

        try:
            LOGIN_CLICK = self.is_visible(self.YOP_MAGICLINK_BTN)
            LINK_CLICK = self.is_visible(self.YOP_MAGIC_LINK)
            if LOGIN_CLICK.is_displayed() and LOGIN_CLICK.is_enabled():
                LOGIN_CLICK.click()

            elif LINK_CLICK.is_displayed():
                LINK_CLICK.click()

            else:
                print("NO LINK AND BUTTON FOUND")        
        except:
            SIGNUP_LINK_CLICK = self.is_visible(self.SIGNUP_LINK)
            if SIGNUP_LINK_CLICK.is_displayed():
                SIGNUP_LINK_CLICK.click()
                print(self.driver.title)

            else:  
                print("NO LINK AND BUTTON FOUND")  
              
        time.sleep(2)
        self.driver.close()


import time
from POMAKRU.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

from POMAKRU.Config.config import TestData

class LoginPage(BasePage):

    """CREATING LOCATORS OF AKRU"""

    ACCEPT_COOKIES=(By.XPATH,'//*[@id="very-specific-design"]/div/div[2]/div[1]/button[1]')
    LOGIN_BTN=(By.ID,'navbar-header-sticky-login')
    SELECT_DROPDOWN=(By.XPATH,'//*[@id="navbar-header-sticky-login"]/div/div/div/div/button')
    WALLET_BOX=(By.CLASS_NAME,'donwload-btn')
    EMAIL=(By.ID,'navbar-magic-email')
    SEND_BTN=(By.XPATH,'//*[@id="navbar-magic-next"]')
    

    """CREATING LOCATORS OF YOPMAIL"""

    YOP_EMAIL_FIELD=(By.CLASS_NAME,'ycptinput')
    YOP_SEND_BTN=(By.XPATH,'//*[@id="refreshbut"]/button/i')
    YOP_FRAME=(By.ID,'ifmail')
    YOP_MAGICLINK_BTN=(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')

    """CONSTRUCTOR"""
    def __init__(self, driver):

        """INHERIT BASE CLASS"""
        super().__init__(driver)
        

    
    """CREATING PAGE ACTIONS"""
    def Login(self,email):
        self.driver.get(TestData.AKRU_URL)
        self.driver.maximize_window()

        """ ASSIGNING INDEX 0 TO AKRU WINDOW"""
        window_before = self.driver.window_handles[0]


        """ RUNNING SCRIPT TO THE CURRENT WINDOW"""
        self.driver.execute_script("window.open()")

        """ PERFORM ACTIONS ON ELEMENTS"""
        self.do_click(self.ACCEPT_COOKIES)
        self.do_click(self.LOGIN_BTN)
        self.do_click(self.SELECT_DROPDOWN)
        self.do_click(self.WALLET_BOX)
        self.do_send_keys(self.EMAIL,email)
        self.do_click(self.SEND_BTN)
        time.sleep(8)

        ################ YOPMAIL WINDOW ############

        """ ASSIGNING INDEX 1 TO YOPMAIL WINDOW"""
        self.driver.switch_to.window(self.driver.window_handles[1])    
        self.driver.get(TestData.YOPMAIL_URL)
        self.do_send_keys(self.YOP_EMAIL_FIELD,email)
        self.do_click(self.YOP_SEND_BTN)
        self.driver.switch_to.frame(self.is_visible(self.YOP_FRAME))
        self.do_click(self.YOP_MAGICLINK_BTN)
        time.sleep(2)
        self.driver.close()

        """ AFTER CLOSING WINDOW 1 YOPMAIL, NOW MAGIC LINK WILL BE OPEN ON INDEX 1"""
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(20)
        self.driver.close()

        """ SWITCHING BACK TO WINDOW 0"""
        self.driver.switch_to.window(window_before)
        time.sleep(12)



    

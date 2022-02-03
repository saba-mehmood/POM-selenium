import re
from POMAKRU.Config.config import TestData
from POMAKRU.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from POMAKRU.Pages.YopMailPage import YopmailPage
import time


class SignUp(BasePage):

    """CREATING LOCATORS OF AKRU SIGNUP"""
    GET_STARTED = (By.CLASS_NAME,'primary-btn')
    YES_RADIO_BTN = (By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/div/label[1]/span[1]/span[1]/input')
    CONTINUE_BTN = (By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/button')
    SELECT_THIS_PLAN_BTN_1 = (By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button')
    SELECT_THIS_PLAN_BTN_2 = (By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button')
    FIRST_NAME = (By.NAME,'firstName')
    LAST_NAME = (By.NAME,'lastName')
    EMAIL = (By.NAME,'email')
    INDIVIDUAL_BTN = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/fieldset/div/label[1]/span[2]')
    CHECK_BOX = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/div[4]/label/span[1]/span[1]/input')
    AGREE_CONTINUE = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/button')
    
    """ CONTACT INFO LOCATORS"""
    ADDRESS = (By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    COUNTRY = (By.NAME,'citizenshipLabel')
    COUNTRY_NAME = ('United States')
    STATE = (By.NAME,'stateName')
    STATE_NAME = ('Alabama')
    CITY = (By.NAME,'city')
    ZIP_CODE = (By.NAME,'zipCode')
    NUMBER = (By.NAME,'number')
    OTP = (By.NAME,'otp')
    VERIFY_BTN = (By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[6]/div/div/div[2]/button')
    DATE_PICKER = (By.XPATH," //input[contains(@value,'08/18/2004')]")
    SSN = (By.NAME,'securityNumber')
    CONTINUE_STEP2 = (By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[2]/div/div/div/button')
    
    """ STEP 3  LOCATORS"""
    SKIP_BTN = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button')
    
    """ STEP 4  LOCATORS"""
    VERIFY_BTN1 = (By.NAME,'point1')
    VERIFY_BTN2 = (By.NAME,'point2')
    VERIFY_BTN3 = (By.NAME,'point3')
    VERIFY_CONTINUE_BTN = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/div[2]/div/div/button')
    
    """CONNECT WALLET STEP"""
    CONNECT_BTN1 = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button')
    CONNECT_BTN2 = (By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button')
    CONNECT_BTN3 = (By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div[2]/div[1]')

    """OTP LOCATOR"""
    OTP_TEXT = (By.XPATH,'/html/body/pre')
    
    ##################################### END OF LOCATORS #############################################

    """CONSTRUCTOR"""
    def __init__(self, driver):

        """INHERIT BASE CLASS"""
        super().__init__(driver)

    """CREATING PAGE ACTIONS"""
    def Signup(self,firstName,lastName,email,address,city,zipcode,number,ssn):

        self.driver.get(TestData.AKRU_URL)
        window_before = self.driver.window_handles[0]
        self.do_click(self.GET_STARTED)
        self.do_click(self.YES_RADIO_BTN)
        self.do_click(self.CONTINUE_BTN)
        self.do_click(self.SELECT_THIS_PLAN_BTN_1)
        self.do_click(self.SELECT_THIS_PLAN_BTN_2)

        self.do_send_keys(self.FIRST_NAME,firstName)
        self.do_send_keys(self.LAST_NAME,lastName)
        self.do_send_keys(self.EMAIL,email)
        self.do_click(self.INDIVIDUAL_BTN)
        self.do_click(self.YES_RADIO_BTN)
        self.do_click(self.AGREE_CONTINUE)


        """CALLING YOPMAILPAGE METHOD"""
        self.yopmail=YopmailPage(self.driver)
        self.yopmail.Yopmail(TestData.EMAIL_SIGNUP)
            
        """ CONTACT INFO"""
        contact_window=self.driver.switch_to.window(self.driver.window_handles[1])
        self.do_send_keys(self.ADDRESS,address)
        select = Select(self.is_visible(self.COUNTRY))
        select.select_by_visible_text(self.COUNTRY_NAME)

        select = Select(self.is_visible(self.STATE))
        select.select_by_visible_text(self.STATE_NAME)

        self.do_send_keys(self.CITY,city)
        self.do_send_keys(self.ZIP_CODE,zipcode)
        self.do_send_keys(self.NUMBER,number)
        self.do_click(self.VERIFY_BTN)

        """ OTP"""
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get(TestData.OTP)
        otp_value = self.is_visible(self.OTP_TEXT)

        """USING REGULAR EXPRESSION TO REMOVING TEXT FROM SENTENCE AND GETTING ONLY NUMBERS"""
        value = int(re.sub(r"[^\d.]", "", otp_value.text))
        print(value)

        """GETTING LAST 4 NUMBERS FROM WHOLE SENTENCE OF OTP"""
        code=int(str(value)[-4:])
        print("value: %s" % code)
        self.driver.close()

        """SWICHING BACK TO CONTACT INFO AND ENTER OTP NUMBER"""
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.do_send_keys(self.OTP,code)

        """DATE PICKER"""
        datee = self.is_visible(self.DATE_PICKER)
        datee.click()
        datee.send_keys(Keys.CONTROL, "a")  
        datee.send_keys("08/18/2002")  
        time.sleep(4)

        self.do_send_keys(self.SSN,ssn)
        self.do_click(self.CONTINUE_STEP2)
        time.sleep(8)
        
        """STEP 3 SKIP BTN"""
        self.do_click(self.SKIP_BTN)
        time.sleep(4)

        """VERIFY STEP"""
        self.do_click(self.VERIFY_BTN1)
        self.do_click(self.VERIFY_BTN2)
        self.do_click(self.VERIFY_BTN3)
        self.do_click(self.VERIFY_CONTINUE_BTN)
        time.sleep(4)

        """CONNECT WALLET STEP"""
        self.do_click(self.CONNECT_BTN1)
        time.sleep(5)
        self.do_click(self.CONNECT_BTN2)
        self.do_click(self.CONNECT_BTN3)
        time.sleep(2)

        """CALLING YOPMAILPAGE METHOD"""
        self.yopmail=YopmailPage(self.driver)
        self.yopmail.Yopmail(TestData.EMAIL_SIGNUP)
        
        
 

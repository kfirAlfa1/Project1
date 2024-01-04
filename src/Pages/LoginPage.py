from selenium.webdriver.common.by import By
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config


from Pages.BasePage import BasePage
from Pages.MainPage import MainPage

class LoginPage(BasePage):
    """Locators
    """
    USER_NAME= (By.ID,"user-name")
    PASSWORD= (By.ID,"password")
    LOGIN_BUTTON=(By.ID,"login-button")
    TITLE=(By.CLASS_NAME,"login_logo")
    ERROR_IN_LOGIN= (By.CLASS_NAME,"error-message-container")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config.TestData.BASE_URL)
        
    def get_title(self):
        return self.wait_for_visibility_of_element(self.TITLE).text 

    def do_login(self,usernmae,password):
        self.do_send_keys(self.USER_NAME,usernmae)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON) 
        return MainPage(self.driver)   
    
    def get_error(self):
       text = self.get_text(self.ERROR_IN_LOGIN)
       return text   

    def get_locked_user_error(self):
        text = self.driver.find_element(By.XPATH,"//*[contains(text(), 'is user has been locked out')]").text
        return text
   
    def visabilty_of_user_input_field(self):
        return self.wait_for_visibility_of_element(self.USER_NAME)
    
    def visabilty_of_password_input_field(self):
        return self.wait_for_visibility_of_element(self.PASSWORD)   

    def visabilty_of_login_button(self):
        return self.wait_for_visibility_of_element(self.LOGIN_BUTTON)            
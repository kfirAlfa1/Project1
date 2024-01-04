from selenium.webdriver.common.by import By
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

from Pages.BasePage import BasePage
from Pages.CartPage import CartPage
from Pages.PaymentPage import PaymentPage

class DetailsPage(BasePage):
    """Locators
    """
    FIRST_NAME=(By.ID,"first-name")
    LAST_NAME=(By.ID,"last-name")
    ZIP_CODE=(By.ID,"postal-code")
    TITLE=(By.CLASS_NAME,"title")
    CANCEL=(By.ID,"cancel")
    CONTINUE_BUTTON=(By.ID,"continue")
    ERROR_MASSAGE=(By.CLASS_NAME,"error-message-container")
    

    def get_title(self):
      title= self.get_text(self.TITLE)
      return title
    
    def __init__(self, driver):
        super().__init__(driver) 

    def get_error_massage(self):
        return self.wait_for_visibility_of_element(self.ERROR_MASSAGE).text

    def visabilty_of_last_name_input_field(self):
        return self.wait_for_visibility_of_element(self.LAST_NAME)

    def visabilty_of_first_name_input_field(self):
        return self.wait_for_visibility_of_element(self.FIRST_NAME)
    
    def visabilty_of_zip_code_input_field(self):
        return self.wait_for_visibility_of_element(self.ZIP_CODE)
    
    def visabilty_of_title(self):
        return self.wait_for_visibility_of_element(self.TITLE)
          
    def fill_details(self,firstName,lastName,zip):
        self.do_send_keys(self.FIRST_NAME,firstName)
        self.do_send_keys(self.LAST_NAME,lastName)
        self.do_send_keys(self.ZIP_CODE,zip)

    def verifiy_details(self):
     firstName=self.wait_for_visibility_of_element(self.FIRST_NAME)
     lastName=self.wait_for_visibility_of_element(self.LAST_NAME)
     zip=self.wait_for_visibility_of_element(self.ZIP_CODE)
     if firstName.get_attribute('value').isalpha() and\
        lastName.get_attribute('value').isalpha() and zip.get_attribute('value').isdigit():
        return True
     else:
        return False
  
    def go_to_cart_page(self):
        self.do_click(self.CANCEL)
        return CartPage(self.driver)

    def go_to_payment_summery_page(self):
         self.do_click(self.CONTINUE_BUTTON) 
         return PaymentPage(self.driver)   
    
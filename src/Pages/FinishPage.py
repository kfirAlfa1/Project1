from selenium.webdriver.common.by import By
import sys
import time

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config


from Pages.BasePage import BasePage
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage

class FinishPage(BasePage):
    """Locators
    """
    BACK_HOME_BUTTON=(By.ID,"back-to-products")
    ICON=(By.CLASS_NAME,"pony_express")
    TITLE=(By.CLASS_NAME,"title")
    DESCRIPTION=(By.CLASS_NAME,"complete-text")
    THANK_YOU_MASSAGE=(By.CLASS_NAME,"complete-header")


    def __init__(self, driver):
        super().__init__(driver) 

    def get_icon_location(self):
      elementLocation= self.wait_for_visibility_of_element(self.ICON).location
      return elementLocation
    
    def get_title(self):
      return self.get_text(self.TITLE)

    def get_description(self):
        return self.get_text(self.DESCRIPTION)
    
    def get_thank_you_massage(self):
        return self.get_text(self.THANK_YOU_MASSAGE)
    
    def visabilty_of_icon(self):
        return self.wait_for_visibility_of_element(self.ICON)

    def visabilty_of_description(self):
        return self.wait_for_visibility_of_element(self.DESCRIPTION)
   
    def go_to_home_page(self):
        self.do_click(self.BACK_HOME_BUTTON)
        return MainPage(self.driver)
     
    def verify_cart_is_empty(self):
       cartPage=CartPage(self.driver)
       return cartPage.verify_empty_cart()   
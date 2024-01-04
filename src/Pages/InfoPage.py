from selenium.webdriver.common.by import By
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

from Pages.MainPage import MainPage
from Pages.BasePage import BasePage
from Pages.CartPage import CartPage

class InfoPage(BasePage):
    """Locators
    """
    TITLE_OF_PAGE=(By.ID,"back-to-products")
    NAME_OF_PRODUCT= (By.CLASS_NAME,"large_size")
    SUMMERY_ON_PRODUCT= (By.CLASS_NAME, "inventory_details_desc large_size")
    PRICE= (By.CLASS_NAME,"inventory_details_price")
    IMAGE=(By.CLASS_NAME,"inventory_details_img")
    BACK_TO_PRODUCT_BUTTON= (By.ID,"back-to-products")
    ADD_TO_CART= (By.CLASS_NAME,"btn_inventory")
    CART_BUTTON= (By.CLASS_NAME,"shopping_cart_link")
    DESCRIPTION=(By.CLASS_NAME,"inventory_details_desc")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
      title= self.get_text(self.TITLE_OF_PAGE)
      return title
    
    def get_name_of_product(self):
     nameOfProduct= self.get_text(self.NAME_OF_PRODUCT) 
     return nameOfProduct
    
    def get_price_of_product(self):
     priceOfProduct= self.wait_for_visibility_of_element(self.PRICE).text 
     return priceOfProduct
    
    def get_description_of_product(self):
     descriptionOfProduct= self.wait_for_visibility_of_element(self.DESCRIPTION).text 
     return descriptionOfProduct
    
    def get_src_of_image_of_product(self):
      mainPage=MainPage(self.driver) 
      element= self.wait_for_visibility_of_element(self.IMAGE)
      src=element.get_attribute("src")
      return mainPage.split_string_of_images(src)
    
    def add_to_cart(self):
      self.do_click(self.ADD_TO_CART)   

    def remove_from_cart(self):
      if "Remove"== self.get_text(self.ADD_TO_CART):
         self.do_click(self.ADD_TO_CART)

    def verify_added_to_cart(self):
      if "Remove"== self.get_text(self.ADD_TO_CART):
        return True
      else:
        return False
     
    def verify_removed_from_cart(self):
      if "Add to cart"== self.get_text(self.ADD_TO_CART):
        return True
      else:
        return False  
      
    #Check if the image cordinate with the product
    def verify_right_image(self):
     src=self.get_src_of_image_of_product()
     product=self.get_name_of_product().lower()
     src= set(src.split())
     if '(' in product and ')' in product:
        product = product.replace('(', '').replace(')', '') 
     product=set(product.split())
     commonWords=src.intersection(product)
     if commonWords != None:
       return True
     else:
      print(self.productThatRemoved+"didnt removed from cart")
      return False

    def verify_right_product(self,product):
     productInWebsite =self.get_name_of_product().lower()
     product=product.lower()
     if '(' in productInWebsite and ')' in productInWebsite:
        product = product.replace('(', '').replace(')', '')
        productInWebsite=productInWebsite.replace('(', '').replace(')', '')
     if product in productInWebsite:
       return True
     return False

    def go_to_main_page(self):
     self.do_click(self.BACK_TO_PRODUCT_BUTTON)
     return MainPage(self.driver) 
    
    def go_to_cart_page(self):
     self.do_click(self.CART_BUTTON)
     return CartPage(self.driver) 
  
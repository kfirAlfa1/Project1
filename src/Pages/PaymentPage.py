from selenium.webdriver.common.by import By
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

from Pages.BasePage import BasePage
from Pages.FinishPage import FinishPage
from Pages.CartPage import CartPage


class PaymentPage(BasePage):
    """Locators
    """
    TITLE_OF_PAGE=(By.CLASS_NAME,"title")
    TOTAL_PRICE= (By.CLASS_NAME,"summary_total_label")
    PRODUCTS= (By.CLASS_NAME,"cart_item")
    PAYMENT_INFO=(By.CLASS_NAME,"summary_value_label")
    TAX= (By.CLASS_NAME,"summary_tax_label")
    FINISH_BUTTON=(By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
      title= self.get_text(self.TITLE_OF_PAGE)
      return title

    def get_title_of_products(self):
     cartPage= CartPage(self.driver)
     products=cartPage.get_products_in_cart_as_str()
     return products

    def get_price_of_product(self,nameOfProduct):
     cartPage= CartPage(self.driver)
     price=cartPage.get_price_of_specific_product(nameOfProduct)
     return price
            
    def get_quantity(self,nameOfProduct):
        cartPage=CartPage(self.driver)
        return cartPage.get_quantity(nameOfProduct)
    
    def get_description_of_product(self,nameOfProduct):
        cartPage=CartPage(self.driver)
        return cartPage.get_description_of_product(nameOfProduct)

    def get_total_price(self):
        price= self.wait_for_visibility_of_element(self.TOTAL_PRICE).text
        index=price.find('$')
        price=price[index:]
        return price

    def get_tax(self):
     tax= self.wait_for_visibility_of_element(self.TAX)
     return tax.text
    
    def get_shipping_info(self):
     shippingInfo= self.wait_for_all_elements(self.PAYMENT_INFO)
     return shippingInfo[1].text

    def get_list_of_products(self):
        return self.wait_for_all_elements(self.PRODUCTS)       

    def get_card_payment_information(self):
     paymentInfo= self.wait_for_all_elements(self.PAYMENT_INFO)
     return paymentInfo[0].text
    
    def convert_to_number(self,price):
     price = price.split('$')[-1].strip()
     price=float(price)
     price=round(price,3)
     return price
       

    def verify_correct_total_price(self):
     from Pages.MainPage import MainPage
     cartPgae=CartPage(self.driver)
     mainPage=MainPage(self.driver)
     pricesAsStr=cartPgae.get_prices_of_productes()
     prices=mainPage.convert_element_list_to_number_list(pricesAsStr)
     totalSum = self.get_total_price()
     totalSum=self.convert_to_number(totalSum)
     tax=self.get_tax()
     tax=self.convert_to_number(tax)
     sumOfTaxAndPrice=sum(prices)+tax
     sumOfTaxAndPrice=round(sumOfTaxAndPrice,3)
     if sumOfTaxAndPrice== totalSum:
      return True
     else:
        return False
     
    def go_to_info_page(self,nameOfProduct):
        cartPage= CartPage(self.driver)
        return cartPage.go_to_info_page(nameOfProduct)

    def go_to_cart_page(self):
        from Pages.MainPage import MainPage
        mainPage= MainPage(self.driver)
        return mainPage.go_to_cart_page()

    def finish_the_purchase(self):
     self.do_click(self.FINISH_BUTTON)
     return FinishPage(self.driver)
   
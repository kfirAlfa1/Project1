import pytest
import sys
import unittest

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

#From Pages
import MainPage
import LoginPage
import DetailsPage
import PaymentPage
import CartPage
import InfoPage
import FinishPage

from test_base import BaseTest
from Tests.test_MainPage import Test_MainPage 


class Test_PaymentPage(BaseTest):
   
   def go_to_payment_page_with_products(self,username):
     mainPage= Test_MainPage.go_to_main_page(self,username)
     mainPage.remove_from_cart()
     mainPage.add_to_cart_specific_product("Bike")
     mainPage.add_to_cart_specific_product("Jacket")
     cartPage=mainPage.go_to_cart_page()
     detailsPage= cartPage.go_to_details_page()
     detailsPage.fill_details(config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP)
     return detailsPage.go_to_payment_summery_page()
   
   def assert_one_function_without_param_with_comparison(self,username,func1,comparison,error):
     try: 
      assert func1() == comparison 
     except Exception:
      error =error 
      pytest.fail(f"Failed for user '{username}':{error}")

# #This if statment prevent from all tests to execute when using in one of the assert functions
if __name__ == "__main__":
    unittest.main()
# ################################################    
                  
    @pytest.fixture(params=[
              config.TestData.STANDARD_USER_NAME,
              config.TestData.VISUAL_USER_NAME,
              config.TestData.GLITCH_USER_NAME,
              config.TestData.ERROR_USER_NAME,
          ])

    def username(self, request):
              return request.param


    def test_go_to_info_page(self,username):
          paymentPage= self.go_to_payment_page_with_products(username)
          infoPage=paymentPage.go_to_info_page("Bike")
          Test_MainPage.assert_move_from_page(self,username,infoPage.get_title,config.TestData.INFO_PAGE_TITLE,InfoPage.InfoPage(self.driver))


    def test_correct_total_price(self,username):
          paymentPage=self.go_to_payment_page_with_products(username)
          Test_MainPage.assert_one_function_without_param(self, username, paymentPage.verify_correct_total_price,"Inccorect price")
        

    def test_correct_payment_information(self,username):
          paymentPage=self.go_to_payment_page_with_products(username)
          self.assert_one_function_without_param_with_comparison(username,paymentPage.get_shipping_info,config.TestData.SHIPPING_INFO,"Worng shipping information")
      

    def test_finish_the_purchase(self,username):
          paymentPage=self.go_to_payment_page_with_products(username)
          finishPage=paymentPage.finish_the_purchase()
          Test_MainPage.assert_move_from_page(self,username,finishPage.get_title,config.TestData.FINISH_PAGE_TITLE,FinishPage.FinishPage(self.driver))
import pytest
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

#From Pages
import MainPage
import LoginPage

from test_base import BaseTest
from Tests.test_PaymentPage import Test_PaymentPage
from Tests.test_MainPage import Test_MainPage


class Test_FinishPage (BaseTest):
   
   @pytest.fixture(params=[
          config.TestData.STANDARD_USER_NAME,
          config.TestData.VISUAL_USER_NAME,
          config.TestData.GLITCH_USER_NAME,
          ])

   def username(self, request):
              return request.param
   
   def go_to_payment_page_with_products(self,username):
     paymentPage = Test_PaymentPage.go_to_payment_page_with_products(self,username)
     return  paymentPage.finish_the_purchase()               

   def test_icon_location(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    Test_PaymentPage.assert_one_function_without_param_with_comparison(self,username,finishPage.get_icon_location,config.TestData.ICON_LOCATION_FINISH_PAGE,"The cart icon isn't in his right position")
   

   def test_messages_describe(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    Test_PaymentPage.assert_one_function_without_param_with_comparison(self,username,finishPage.get_description,config.TestData.DESCRIBE_MASSAGE,"The cart description is worng")

   def test_messages(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    Test_PaymentPage.assert_one_function_without_param_with_comparison(self,username,finishPage.get_thank_you_massage,config.TestData.MESSAGE_OF_COMPLETE,"The massage of thank you is worng")


   def test_messages(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    Test_PaymentPage.assert_one_function_without_param_with_comparison(self,username,finishPage.get_thank_you_massage,config.TestData.MESSAGE_OF_COMPLETE,"The massage of thank you is worng")


   def test__cart_is_empty(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    Test_MainPage.assert_one_function_without_param(self, username, finishPage.verify_cart_is_empty,"The cart is not empty after the purchase")


   def test_go_to_home_page(self,username):
    finishPage=self.go_to_payment_page_with_products(username)
    mainPage=finishPage.go_to_home_page()
    Test_MainPage.assert_move_from_page(self, username, mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))
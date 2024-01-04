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
import CartPage
import PaymentPage

from test_base import BaseTest
from Tests.test_CartPage import Test_CartPage
from Tests.test_MainPage import Test_MainPage

class Test_DetailsPage(BaseTest):

   def go_to_details_page(self,username):
     cartPage=Test_CartPage.go_to_cart_page(self,username)
     return cartPage.go_to_details_page()

#This if statment prevent from all tests to execute when using in one of the assert functions
if __name__ == "__main__":
    unittest.main()
################################################                
    @pytest.fixture(params=[
          config.TestData.STANDARD_USER_NAME,
          config.TestData.VISUAL_USER_NAME,
          config.TestData.GLITCH_USER_NAME,
          config.TestData.ERROR_USER_NAME,
          config.TestData.PROBLEMATIC_USER_NAME,
      ])

    def username(self, request):
          return request.param


    def test_go_to_cart_page(self,username):
        detailsPage=self.go_to_details_page(username)
        cartPage=detailsPage.go_to_cart_page()
        Test_MainPage.assert_move_from_page(self,username,cartPage.get_title,config.TestData.CART_PAGE_TITLE,CartPage.CartPage(self.driver))

    def test_go_to_payment_summery_page(self,username):
        detailsPage=self.go_to_details_page(username)
        detailsPage.fill_details(config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP)
        paymentPage=detailsPage.go_to_payment_summery_page()
        Test_MainPage.assert_move_from_page(self,username,paymentPage.get_title,config.TestData.PAYMENT_PAGE_TITLE,PaymentPage.PaymentPage(self.driver))




    @pytest.mark.parametrize(
        "firstName,lastName,zip",
        [
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.ZIP,config.TestData.ZIP),
        (config.TestData.ZIP,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.FIRST_NAME),
      ])

    def test_fill_details(self,firstName,lastName,zip):
        detailsPage=self.go_to_details_page(config.TestData.STANDARD_USER_NAME)
        detailsPage.fill_details(firstName,lastName,zip)
        Test_MainPage.assert_one_function_without_param(self, config.TestData.STANDARD_USER_NAME, detailsPage.verifiy_details,"First and last names must contain letters, while zip codes must contain only numbers")
      

    # # Check all users error massages 
        
    @pytest.mark.parametrize(
        "firstName,lastName,zip",
        [
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.EMPTY,config.TestData.ZIP),
        (config.TestData.EMPTY,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.EMPTY),
      ])

    def test_errors_of_unfill_fileds(self,firstName,lastName,zip):
        detailsPage=self.go_to_details_page(config.TestData.STANDARD_USER_NAME)
        detailsPage.fill_details(firstName,lastName,zip)
        paymentPage=detailsPage.go_to_payment_summery_page()  
        try:
          assert paymentPage.get_title() == config.TestData.PAYMENT_PAGE_TITLE
        except Exception:
          error =detailsPage.get_error_massage()
          pytest.fail(f"Failed for user '{config.TestData.STANDARD_USER_NAME}':{error}") 
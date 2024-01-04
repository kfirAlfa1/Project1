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
import InfoPage

from test_base import BaseTest
from Tests.test_MainPage import Test_MainPage


class Test_CartPage(BaseTest):

  @pytest.fixture(params=[
        config.TestData.STANDARD_USER_NAME,
        config.TestData.VISUAL_USER_NAME,
        config.TestData.GLITCH_USER_NAME,
        config.TestData.ERROR_USER_NAME,
        config.TestData.PROBLEMATIC_USER_NAME,
    ])

  def username(self, request):
        return request.param

  def go_to_cart_page(self,username):
     mainPage=Test_MainPage.go_to_main_page(self,username)
     return  mainPage.go_to_cart_page()

  def assert_three_functions_with_one_param(self, username, func1,func2,func3,param1,error1,error2):
       try: 
         if func1(param1) == True :
             func2(param1)
             assert func3(param1)
         else:
             print(error2)
             pytest.fail(f"Failed for user '{username}'")    
       except Exception:
                print(error1)
                pytest.fail(f"Failed for user '{username}'") 

#This if statment prevent from all tests to execute when using in one of the assert functions
if __name__ == "__main__":
    unittest.main()
################################################                

  

    def test_remove_all_products_from_cart(self,username):
        mainPage=Test_MainPage.go_to_main_page(self,username)
        mainPage.add_to_cart_specific_product("Bike")
        mainPage.add_to_cart_specific_product("Jacket")
        cartPage=mainPage.go_to_cart_page()
        cartPage.remove_all_products_from_cart()
        Test_MainPage.assert_one_function_without_param(self,username,cartPage.verify_empty_cart,"The following products didnt removed from cart: ")

    def test_remove_spesific_product_from_cart(self,username):
        mainPage=Test_MainPage.go_to_main_page(self,username)
        product="Jacket"
        mainPage.remove_from_cart()
        mainPage.add_to_cart_specific_product(product)
        cartPage=mainPage.go_to_cart_page()
        self.assert_three_functions_with_one_param(username,cartPage.verify_added_to_cart,cartPage.remove_specific_product_from_cart,
                                                  cartPage.verify_removed_from_cart,product,"The product didn't removed from cart","The product didn't added to cart")

    def test_add_spesific_product_from_cart(self,username):
        mainPage=Test_MainPage.go_to_main_page(self,username)
        product="Jacket"
        mainPage.remove_from_cart()
        mainPage.add_to_cart_specific_product(product)
        cartPage=mainPage.go_to_cart_page()  
        Test_MainPage.assert_one_function_with_param(self,username,cartPage.verify_added_to_cart,product,"The product didn't added to cart")
                                                  

    def test_from_cart_page_to_details_page(self,username):
        cartPage=self.go_to_cart_page(username)
        detailsPage=cartPage.go_to_details_page()
        Test_MainPage.assert_move_from_page(self,username,detailsPage.get_title,config.TestData.DETAILS_PAGE_TITLE,DetailsPage.DetailsPage(self.driver))


    def test_from_cart_page_to_main_page(self,username):
        cartPage=self.go_to_cart_page(username)
        mainPage=cartPage.go_to_main_page()
        Test_MainPage.assert_move_from_page(self,username,mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))


    def test_from_cart_page_to_info_page(self,username):
        mainPage=Test_MainPage.go_to_main_page(self,username)
        product="Bike"
        mainPage.remove_from_cart()
        mainPage.add_to_cart_specific_product(product)
        cartPage=mainPage.go_to_cart_page()
        infoPage=cartPage.go_to_info_page(product)
        Test_MainPage.assert_move_from_page(self,username,infoPage.get_title,config.TestData.INFO_PAGE_TITLE,InfoPage.InfoPage(self.driver))
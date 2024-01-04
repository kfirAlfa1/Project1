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
import InfoPage
import CartPage

from test_base import BaseTest
from  Tests.test_MainPage import Test_MainPage


class Test_InfoPage(BaseTest):

    @pytest.fixture(params=[
            config.TestData.STANDARD_USER_NAME,
            config.TestData.VISUAL_USER_NAME,
            config.TestData.GLITCH_USER_NAME,
            config.TestData.ERROR_USER_NAME,
            config.TestData.PROBLEMATIC_USER_NAME,
        ])

    def username(self, request):
            return request.param

    def go_to_info_page(self,username,product):
     self.loginPage=LoginPage.LoginPage(self.driver)
     mainPage=self.loginPage.do_login(username,config.TestData.PASSWORD)
     return mainPage.go_to_info_page(product)

    def assert_two_functions_with_param_for_func1(self, username, func1,func2,param1,error1,error2):
        try: 
         if func1(param1) == True :
             assert func2()
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


    def test_add_to_cart(self,username):
     infoPage=self.go_to_info_page(username,"Jacket")
     infoPage.remove_from_cart()
     infoPage.add_to_cart()
     self.assert_two_functions_with_param_for_func1(username,infoPage.verify_right_product,infoPage.verify_added_to_cart,"Jacket","Didn't reach the desire page","The product has not been added to the cart")


    def test_remove_from_cart(self,username):
     infoPage=self.go_to_info_page(username,"Jacket")
     infoPage.remove_from_cart()
     infoPage.add_to_cart()
     infoPage.remove_from_cart()
     self.assert_two_functions_with_param_for_func1(username,infoPage.verify_right_product,infoPage.verify_removed_from_cart,"Jacket","Didn't reach the desire page","The product has not been removed from cart")


    def test_check_image(self,username):
     infoPage=self.go_to_info_page(username,"Bike")
     self.assert_two_functions_with_param_for_func1(username,infoPage.verify_right_product,infoPage.verify_right_image,"Bike","Didn't reach the desire page","The image and the prodcut are no coordinated") 


    def test_go_to_main_page(self,username):
     infoPage=self.go_to_info_page(username,"Jacket")
     mainPage=infoPage.go_to_main_page()
     Test_MainPage.assert_move_from_page(self,username,mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))

    def test_go_to_cart_page(self,username):
     infoPage=self.go_to_info_page(username,"Jacket")
     cartPage=infoPage.go_to_cart_page()
     Test_MainPage.assert_move_from_page(self,username,cartPage.get_title,config.TestData.CART_PAGE_TITLE,CartPage.CartPage(self.driver))
import pytest
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

#From Conf
import config

#From Pages
import LoginPage
import MainPage

from test_base import BaseTest
from Tests.test_MainPage import Test_MainPage

class Test_LoginPage(BaseTest):

 # Check all users               
    @pytest.mark.parametrize(
     "username, password",
    [#Pass
    (config.TestData.STANDARD_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.PROBLEMATIC_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.GLITCH_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.ERROR_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.VISUAL_USER_NAME, config.TestData.PASSWORD),
    #Fail 
    (config.TestData.STANDARD_USER_NAME, config.TestData.EMPTY_PASSWORD),
    (config.TestData.EMPTY_USER, config.TestData.PASSWORD),
    (config.TestData.LOCKED_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.BLABLA,config.TestData.BLABLA ),
    (config.TestData.EMPTY, config.TestData.EMPTY),
    ])
  
    def test_from_loginPage_to_main_page(self, username, password):
        loginPage = LoginPage.LoginPage(self.driver)
        mainPage = loginPage.do_login(username, password)
        Test_MainPage.assert_move_from_page(self, username, mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))

          

    @pytest.mark.parametrize(
     "username, password",
    [
    #Fail 
    (config.TestData.STANDARD_USER_NAME, config.TestData.EMPTY_PASSWORD),
    (config.TestData.EMPTY_USER, config.TestData.PASSWORD),
    (config.TestData.LOCKED_USER_NAME, config.TestData.PASSWORD),
    (config.TestData.BLABLA,config.TestData.BLABLA ),
    (config.TestData.EMPTY, config.TestData.EMPTY),
    ])
  
    def test_error(self, username, password):
        loginPage = LoginPage.LoginPage(self.driver)
        mainPage = loginPage.do_login(username, password)
        try:
            mainPage.get_title()
        except Exception:
         error = loginPage.get_error()
         pytest.fail(f"Failed for user '{username}':{error}") 

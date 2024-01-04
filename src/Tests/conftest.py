import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import os


path = Service(r"C:\\Users\Kfir\Desktop\chromedriver.exe")
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
     web_driver= webdriver.Chrome(service=path)
     time.sleep(2)
     web_driver.maximize_window()
    request.cls.driver= web_driver
    web_driver.implicitly_wait(2)
    yield
    web_driver.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.cls.driver
        test_name = item.name
        screenshot_name = f"screenshot_{test_name}.png"
        driver.save_screenshot(screenshot_name)
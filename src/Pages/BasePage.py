from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self._wait = WebDriverWait(self.driver, 10)

    @property
    def wait(self):
        return self._wait

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_double_click(self, by_locator):
        el = self._wait_until(by_locator)
        action = ActionChains(self.driver)
        action.double_click(el).perform()

    def _wait_until(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))
    
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self,by_locator):
       elemnt=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
       return elemnt.text

    def clear_text(self, by_locator):
        self._wait_until(by_locator).clear()

    def get_length(self, by_locator):
        return len(self._wait_until(by_locator))

    def wait_for_element_to_be_clickable(self, by_locator):
        return self.wait.until(EC.element_to_be_clickable(by_locator))
    
    def wait_for_all_elements(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def wait_for_element_to_disappear(self, by_locator):
        return self.wait.until(EC.invisibility_of_element(by_locator))

    def wait_for_visibility_of_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)) 
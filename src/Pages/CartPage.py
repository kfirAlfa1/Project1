from selenium.webdriver.common.by import By
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

from Pages.BasePage import BasePage


class CartPage(BasePage):
    """Locators
    """
    TITLE_OF_PAGE=(By.CLASS_NAME,"title")
    QUANTITY="cart_quantity"
    NAME_OF_PRODUCT= (By.CLASS_NAME,"cart_item")
    CONTINUE_SHOPPING_BUTTON=(By.ID,"continue-shopping")
    CHECK_OUT_BUTTON=(By.ID,"checkout")
    REMOVE_BUTTON= (By.CLASS_NAME,"cart_button")
    PRODUCTS_ELEMENT=(By.CLASS_NAME,"cart_item")
    CANCEL_BUTTON=(By.ID,"cancel")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
      title= self.get_text(self.TITLE_OF_PAGE)
      return title
    
    def get_productes_in_cart_as_elements(self):
     try:
      listOfProductsAsElements=self.wait_for_all_elements(self.NAME_OF_PRODUCT)
      return listOfProductsAsElements
     except Exception:
       return None
  
    def get_products_in_cart_as_str(self):
     listOfElements=self.get_productes_in_cart_as_elements()
     listOfProductsAsStr=[]
     if listOfElements != None:
      for i in range(len(listOfElements)):
        fatherElement=listOfElements[i].find_element(By.CLASS_NAME,"cart_item_label")
        nameOfProduct=fatherElement.find_element(By.CLASS_NAME,"inventory_item_name").text
        listOfProductsAsStr.append(nameOfProduct)
     return listOfProductsAsStr


    def get_quantity(self,product):
     fatherElement=self.find_father_element_cart(product)
     quantity =fatherElement.find_element(By.CSS_SELECTOR,".cart_quantity").text
     return quantity  
    
    #This function returns the prices all products by the order that are arrange in the cart
    def get_prices_of_productes(self):
        listOfProductsAsElements=self.get_productes_in_cart_as_elements()
        listOfPrices=[]
        for i in range(len(listOfProductsAsElements)):
         price=listOfProductsAsElements[i].find_element(By.CSS_SELECTOR,".inventory_item_price").text
         listOfPrices.append(price)
        return listOfPrices 

    def get_price_of_specific_product(self,product):
      fatherElement=self.find_father_element_cart(product)
      price=fatherElement.find_element(By.CSS_SELECTOR,".inventory_item_price").text
      return price 
    
    def get_description_of_product(self,product):
      fatherElement=self.find_father_element_cart(product)
      price=fatherElement.find_element(By.CSS_SELECTOR,".inventory_item_desc").text
      return price 

    #This function return a list of all buttones
    def remove_all_products_from_cart(self):
        listOfProductsAsElements=self.get_productes_in_cart_as_elements()
        for i in range(len(listOfProductsAsElements)):
         temp1=listOfProductsAsElements[i].find_element(By.CLASS_NAME,"cart_item_label")
         temp2=temp1.find_element(By.CLASS_NAME,"item_pricebar")
         button=temp2.find_element(By.CLASS_NAME,"btn_secondary ")
         button.click()

    def remove_specific_product_from_cart(self,productToRemove):
      fatherElement=self.find_father_element_cart(productToRemove)
      temp1=fatherElement.find_element(By.CLASS_NAME,"cart_item_label")
      temp2=temp1.find_element(By.CLASS_NAME,"item_pricebar")
      button=temp2.find_element(By.CLASS_NAME,"btn_secondary ")
      button.click()


    def find_father_element_cart(self,product):
      fatherElement=self.get_productes_in_cart_as_elements()
      listOfStr=self.get_products_in_cart_as_str()
      duplicateList=[]
      for i in range(len(listOfStr)):
        if '(' in listOfStr[i] and ')' in listOfStr[i]:
          listOfStr[i] = listOfStr[i].replace('(', '').replace(')', '') 
        if product.lower() in listOfStr[i].lower():
          duplicateList.append(fatherElement[i])
      if len (duplicateList) == 1:
          return duplicateList[0]
      elif len (duplicateList) > 1:
            print("Please insert 2 words of the name of the product")
            return False
      else:
        print("Couldent find the product")
        return False

    def verify_empty_cart(self):
      if self.get_productes_in_cart_as_elements() != None:
        return False
      else:
       return True

    def verify_removed_from_cart(self,productThatRemoved):
     productsInCart=self.get_products_in_cart_as_str()
     commonWords=any(productThatRemoved in string for string in productsInCart)
     if commonWords :
       return False
     else:
       return True

    def verify_added_to_cart(self,productThatAdded):
     productsInCart=self.get_products_in_cart_as_str()
     commonWords = any(productThatAdded in string for string in productsInCart)
     if commonWords:
       return True
     else:
       return False
     

    def go_to_main_page(self):
     from Pages.MainPage import MainPage
     self.do_click(self.CONTINUE_SHOPPING_BUTTON)
     return MainPage(self.driver)

    def go_to_details_page(self):
     from Pages.DetailsPage import DetailsPage
     self.do_click(self.CHECK_OUT_BUTTON)
     return DetailsPage(self.driver)
    
    def go_to_info_page(self,product):
     from Pages.InfoPage import InfoPage
     fatherElement=self.find_father_element_cart(product)
     sonElement=fatherElement.find_element(By.CLASS_NAME,"cart_item_label")
     sonElement=sonElement.find_element(By.CLASS_NAME,"inventory_item_name")
     sonElement.click()
     return InfoPage(self.driver)



      
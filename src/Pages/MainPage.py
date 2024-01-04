from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.support.ui import Select
import re

sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\Projects\\src\\Tests")

import config

from Pages.BasePage import BasePage

class MainPage(BasePage):
    """Locators
    """
    TITLE_OF_PAGE=(By.CLASS_NAME, "title")
    FHATER_PRODUCT_ELEMENT=(By.CLASS_NAME,"inventory_item_description")
    PRICES= (By.CLASS_NAME, "inventory_item_price")
    SORTED_BY= (By.CLASS_NAME, "active_option")
    IMAGES= (By.CLASS_NAME,"inventory_item_img")
    PRODUCT=(By.CLASS_NAME,"inventory_item")
    NAME_OF_PRODUCT=(By.CLASS_NAME,"inventory_item_name")
    LIST_OF_FILTERS=(By.CSS_SELECTOR,".product_sort_container")
    PRICE_ELEMENT= (By.CLASS_NAME,"pricebar")
    ADD_TO_CART= (By.CLASS_NAME,"btn_inventory")
    SIDE_MANUE= (By.ID,"react-burger-menu-btn")
    LOG_OUT_BUTTON= (By.ID,"logout_sidebar_link")
    CART_BUTTON= (By.CLASS_NAME,"shopping_cart_link") 
    CART_NUM_OF_PRODUCTS=(By.CLASS_NAME,"shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
      title= self.get_text(self.TITLE_OF_PAGE)
      return title
    #Returning the current filter of sorting
    def get_sort_by(self):
      sortByStr = self.get_text(self.SORTED_BY)
      return sortByStr
    
    def get_list_of_prices_as_str(self):
      listOfElements= self.get_list_of_products_as_elements()
      listOfPrices=[]
      for i in range(len(listOfElements)):
         price=listOfElements[i].find_element(By.CSS_SELECTOR,".inventory_item_price").text
         listOfPrices.append(price)
      return listOfPrices
      
    def get_list_of_products_as_elements(self):
      listOfElements= self.wait_for_all_elements(self.PRODUCT)
      return listOfElements
    
    def get_list_of_images(self):
      listOfElements= self.wait_for_all_elements(self.IMAGES)
      listOfImages=[]
      for i in range(len(listOfElements)):
         temp=listOfElements[i].get_attribute("src")
         if temp ==None:
           continue
         else:
           listOfImages.append(listOfElements[i].get_attribute("src"))
      return listOfImages
    
    def get_list_of_products_as_string(self):
       listOfElements= self.get_list_of_products_as_elements()
       listOfProducts=[]
       for i in range(len(listOfElements)):
         titleOfProduct=listOfElements[i].find_element(By.CSS_SELECTOR,".inventory_item_name").text
         listOfProducts.append(titleOfProduct)
       return listOfProducts
       
    def get_icon_of_cart_products_number(self):
      try:
        numOfProducts= len (self.wait_for_all_elements(self.CART_NUM_OF_PRODUCTS))
        return numOfProducts
      except:
        return 0  
      
    def get_icon_of_cart_location(self):
      elementLocation= self.wait_for_visibility_of_element(self.CART_BUTTON).location
      return elementLocation
    
    def get_spesific_button_element(self,fatherElement):
      tempElement1=fatherElement.find_element(By.CLASS_NAME,"inventory_item_description") 
      tempElement2=tempElement1.find_element(By.CLASS_NAME,"pricebar")
      tempElement3=tempElement2.find_element(By.CLASS_NAME,"btn_small")
      return tempElement3 
  
    def get_buttones_as_elements(self):
        fatherElemnts=self.get_list_of_products_as_elements()
        buttonElements=[]
        for i in  range(len(fatherElemnts)):
           button=self.get_spesific_button_element(fatherElemnts[i]) 
           buttonElements.append(button)
        return buttonElements
    
    def get_description_of_specific_product(self,product):
        fatherElemnt=self.find_father_element_main_page(product)
        description=fatherElemnt.find_element(By.CLASS_NAME,"inventory_item_desc").text
        return description
        
      #This function returns the father element of spesific product
    def find_father_element_main_page(self,product):
      fatherElement=self.get_list_of_products_as_elements()
      listOfStr=self.get_list_of_products_as_string()
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
      
    #Converting from list of elemntes to list of strings 
    def convert_element_list_to_text_list(self,listOfElements):
      listToConvert=[]
      for i in range(len(listOfElements)):
         listToConvert.append(listOfElements[i].text)
      return listToConvert
    
    def convert_element_list_to_number_list(self,listOfElements):
      listOfElements=self.remove_dollar_sign(listOfElements)
      numericList = [float(item) for item in listOfElements]
      return numericList
 
    def remove_dollar_sign(self,listOfElements):
      charToRemove = "$"
      listOfPrices=[]
      for i in range(len(listOfElements)):
         listOfPrices.append(listOfElements[i].replace(charToRemove, "")) 
      return listOfPrices   
   #This function removes all the productes from cart
    def remove_from_cart(self):
      buttones= self.get_buttones_as_elements()
      for i in range(len(buttones)):
          if buttones[i].text == "Remove":
            buttones[i].click()

    def remove_specific_product_from_cart(self,productToRemove):
      fatherElement= self.find_father_element_main_page(productToRemove)
      button=self.get_spesific_button_element(fatherElement)
      if button.text == "Remove":
          button.click()
      else:
        print("This product not in cart")

    def split_string_of_images(self,stringToSplit):
    # Remove the protocol part (https://)
     stringToSplitWitoutProtocol = stringToSplit.split("://")[1]
     sections = stringToSplitWitoutProtocol.split("/")
     lastSectionWords = sections[-1].split("-")
     allWords = ' '.join(lastSectionWords)
     return allWords

    def do_log_out(self):
     from Pages.LoginPage import LoginPage
     self.do_click(self.SIDE_MANUE)
     self.do_click(self.LOG_OUT_BUTTON)
     return LoginPage(self.driver)  

    def add_to_cart_specific_product(self,productToAdd):
        fatherElemnt=self.find_father_element_main_page(productToAdd)
        tempElement1=fatherElemnt.find_element(By.CLASS_NAME,"inventory_item_description") 
        tempElement2=tempElement1.find_element(By.CLASS_NAME,"pricebar")
        try:
         addToCartButton=tempElement2.find_element(By.CLASS_NAME,"btn_primary")
         addToCartButton.click()
        except Exception:
          pass
        
   #This function adds all products to the cart  
    def add_to_cart(self):
       buttones= self.get_buttones_as_elements()
       for i in range(len(buttones)):
         if buttones[i].text == "Add to cart":
            buttones[i].click()

    def change_filter_and_verify(self,newFilter):
      temp = self.get_sort_by()
      if newFilter == temp:
        return True
      dropdown = self.wait_for_visibility_of_element(self.LIST_OF_FILTERS)
      select = Select(dropdown) 
      if "low to high" in newFilter:
        select.select_by_value("lohi")
        afterChange = self.get_sort_by()
        return self.verify_filter_changed(temp,afterChange)
      elif "high to low" in newFilter:
        select.select_by_value("hilo")
        afterChange = self.get_sort_by()
        return self.verify_filter_changed(temp,afterChange)
      elif "Z to A" in newFilter:
        select.select_by_value("za")
        afterChange = self.get_sort_by()
        return self.verify_filter_changed(temp,afterChange)
      else:
         select.select_by_value("az")
         afterChange = self.get_sort_by()
         return self.verify_filter_changed(temp,afterChange)
      
    def verify_filter_changed(self,beforeFilter,afterFilter):
      if beforeFilter != afterFilter:
        return True
      return False

    def verify_order_of_prices(self):
      sortBy=self.get_sort_by()
      list=self.get_list_of_prices_as_str()
      list=self.convert_element_list_to_number_list(list)
      tempList=list
      if "low to high" in sortBy:
         tempList.sort()
         if list == tempList:
           return True
         return False
      else:#High to low
         tempList.sort(reverse=True)
         if list == tempList:
          return True
         return False
       
    def verify_order_of_products(self):
      sortBy=self.get_sort_by()
      list=self.get_list_of_products_as_string()
      tempList=list
      if "A to Z" in sortBy:
         tempList.sort()
         if list == tempList:
           return True
         return False
      else:#Z to A
         tempList.sort(reverse=True)
         if list == tempList:
          return True
         return False  
        
    def verify_right_order(self):
     sortBY=self.get_sort_by()
     if "Price" in sortBY:#Ordered by price
       return self.verify_order_of_prices()
     else:#Ordered by name
       if "Name" in sortBY:
         return self.verify_order_of_products() 
       
    def verify_specific_prodcut_added_to_cart(self,productThatAdded):
     fatherElement=self.find_father_element_main_page(productThatAdded)
     buttonElement=self.get_spesific_button_element(fatherElement)
     numberOfItems= self.get_icon_of_cart_products_number()
     if buttonElement.text == "Remove" and numberOfItems !=0 :
      return True
     return False

    def verify_specific_prodcut_removed_from_cart(self,productThatRemoved):
     fatherElement=self.find_father_element_main_page(productThatRemoved)
     buttonElement=self.get_spesific_button_element(fatherElement)
     if buttonElement.text == "Add to cart":
       return  True
     else:
       product= fatherElement.find_element(By.CSS_SELECTOR,".inventory_item_name").text
       return product
    
    def verify_all_prodcuts_added_to_cart(self):
     buttonsList=self.get_buttones_as_elements()
     buttonsList=self.convert_element_list_to_text_list(buttonsList)
     if "Add to cart" not in buttonsList:
       return True
     else:
       listOfProducts=self.get_list_of_products_as_string()
       indexes =[index for index, value in enumerate(buttonsList) if value == "Add to cart"]
       listOfProductsNotAdded=[]
       for i in range(len(indexes)):
         tempNumber=indexes[i]
         tempName=listOfProducts[tempNumber]
         listOfProductsNotAdded.append(tempName)
       return listOfProductsNotAdded
     
    def verify_all_prodcuts_removed_from_cart(self):
     buttonsList=self.get_buttones_as_elements()
     buttonsList=self.convert_element_list_to_text_list(buttonsList)
     if "Remove"  in buttonsList:
       listOfProducts=self.get_list_of_products_as_string()
       indexes =[index for index, value in enumerate(buttonsList) if value == "Remove"]
       listOfProductsNotRemoved=[]
       for i in range(len(indexes)):
         tempNumber=indexes[i]
         tempName=listOfProducts[tempNumber]
         listOfProductsNotRemoved.append(tempName)
       return listOfProductsNotRemoved 
     else:
       return True
     
    def verify_right_images(self):
     listOfImages=self.get_list_of_images()
     products=self.get_list_of_products_as_string()
     uncoordinatedProducts=[]
     counter=0
     for i in range(len(listOfImages)):
      src= self.split_string_of_images(listOfImages[i]).lower()
      product=products[i].lower()
      if '(' in product and ')' in product:
        product = product.replace('(', '').replace(')', '') 
      commonWords = set(src.split()) & set(product.split())
      if len(commonWords)> 0:
        counter=counter+1 
      else:
        uncoordinatedProducts.append(products[i])
     if counter== len(listOfImages):
       return True
     else:
       return uncoordinatedProducts
  
    def go_to_info_page(self,product):
     from Pages.InfoPage import InfoPage
     fatherElement=self.find_father_element_main_page(product)
     buttonElement=fatherElement.find_element(By.CLASS_NAME,"inventory_item_name ")
     buttonElement.click()
     return InfoPage(self.driver)  

    def go_to_cart_page(self):
     from Pages.CartPage import CartPage
     self.do_click(self.CART_BUTTON)
     return CartPage(self.driver)
 
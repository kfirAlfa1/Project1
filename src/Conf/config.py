class TestData:    
    BASE_URL="https://www.saucedemo.com/"

    ##-------------LoginPage--------------------##
    ##------------------------------------------##
    LOGIN_PAGE_TITLE="Swag Labs"
    #Standart User
    STANDARD_USER_NAME="standard_user"
    PASSWORD="secret_sauce"
    #Locked User
    LOCKED_USER_NAME="locked_out_user"
    #Problematic User
    PROBLEMATIC_USER_NAME="problem_user"
    #Glitch User
    GLITCH_USER_NAME= "performance_glitch_user"
    #Error User
    ERROR_USER_NAME= "error_user"
    #Visual User
    VISUAL_USER_NAME="visual_user"
    #Error user for user name and password
    BLABLA="BLABLA"

    EMPTY_PASSWORD= ""
    EMPTY_USER = ""
    EMPTY=""


    #Massages:
    LOCKED_USER_MESSAGE="Sorry, this user has been locked out."
    ERROR_MESSAGE="Username and password do not match any user in this service"
    ERROR_MESSAGE_OF_EMPTY_USER="Epic sadface: Username is required"
    ERROR_MESSAGE_OF_EMPTY_PASSWORD="Epic sadface: Password is required"



    ##-------------MainPage--------------------##
    ##------------------------------------------##
    MAIN_PAGE_TITLE="Products"
    PRICES_FROM_HIGH_TO_LOW="Price (high to low)"
    PRICES_FROM_LOW_TO_HIGH="Price (low to high)"  
    PRODUCTS_FROM_A_TO_Z="Name (A to Z)"
    PRODUCTS_FROM_Z_TO_A ="Name (Z to A)"
    ICON_LOCATION_MAIN_PAGE={'x': 1459, 'y': 10}

    ##-------------DetailsPage--------------------##
    ##------------------------------------------##
    DETAILS_PAGE_TITLE="Checkout: Your Information"
    FIRST_NAME="blabla"
    LAST_NAME="blabla"
    ZIP="123"
    #Massages:
    ERROR_MESSAGE_OF_EMPTY_FIRST_NAME="Error: First Name is required"
    ERROR_MESSAGE_OF_EMPTY_LAST_NAME="Error: Last Name is required"
    ERROR_MESSAGE_OF_EMPTY_POSTAL_CODE="Error: Postal Code is required"


    ##-------------InfoPage--------------------##
    ##------------------------------------------##
    INFO_PAGE_TITLE="Back to products"


    ##-------------PaymentPage--------------------##
    ##------------------------------------------##
    PAYMENT_PAGE_TITLE="Checkout: Overview"
    PAYMENT_INFO="SauceCard #31337"
    SHIPPING_INFO="Free Pony Express Delivery!"



    ##-------------CartPage--------------------##
    ##------------------------------------------##
    CART_PAGE_TITLE="Your Cart"


    ##-------------FinishPage--------------------##
    ##------------------------------------------##
    FINISH_PAGE_TITLE="Checkout: Complete!"
    #Massages:
    MESSAGE_OF_COMPLETE="Thank you for your order!"
    DESCRIBE_MASSAGE="Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    ICON_LOCATION_FINISH_PAGE={'x': 732, 'y': 174}


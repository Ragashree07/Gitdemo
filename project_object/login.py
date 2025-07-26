import time

from selenium.webdriver.common.by import By


class Proceedcheckout:

    def __init__(self,driver):
        self.driver = driver
        self.Entering_Name = By.CSS_SELECTOR, ".search-keyword"
        self.Selecting_Veggies = By.XPATH, "//div[@class='products']/div"
        self.Adding_cart = By.XPATH, "//img[@alt='Cart']"
        self.Checking_out = By.XPATH, "//button[text()='PROCEEDING TO CHECKOUT']"




    def Preferred_veggies(self,vegname):
        self.driver.find_element(*self.Entering_Name).send_keys(vegname)
        time.sleep(2)

    def Select_veggies(self):
        products = self.driver.find_elements(*self.Selecting_Veggies)
        for product in products:
            product.find_element(By.XPATH, "div/button").click()

    def Add_to_cart(self):
        self.driver.find_element(*self.Adding_cart).click()

    def Checkout(self):
        self.driver.find_element(*self.Checking_out).click()



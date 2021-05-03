from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
    Checkout_button1 = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def Checkout_button(self):
        return self.driver.find_element(*Checkout.Checkout_button1)

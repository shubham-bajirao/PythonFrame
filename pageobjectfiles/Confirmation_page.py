from selenium.webdriver.common.by import By


class Confirmation:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element_by_css_selector("input[id='country']").send_keys("ind")
    #self.driver.find_element_by_link_text("India").click()
    #self.driver.find_element_by_css_selector("input[type='submit']").click()
    Confirmation1 = (By.CSS_SELECTOR, "input[id='country']")
    Confirmation2 = (By.LINK_TEXT, "India")
    Confirmation3 = (By.CSS_SELECTOR, "input[type='submit']")


    def Confirmation4(self):
        return self.driver.find_element(*Confirmation.Confirmation1)

    def Confirmation5(self):
        return self.driver.find_element(*Confirmation.Confirmation2)

    def Confirmation6(self):
        return self.driver.find_element(*Confirmation.Confirmation3)
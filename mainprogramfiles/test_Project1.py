import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from PytestFramework.pageobjectfiles.Checkout_page import Checkout
from PytestFramework.pageobjectfiles.Confirmation_page import Confirmation
from PytestFramework.Utilities2.BaseClass1 import BaseClass2
#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass2):
    def test_begin(self):
        #Click on shop button
        #time.sleep(5)

        self.driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()
        #page 1 Shoppage
        #finding all the mobiles available
        products = self.driver.find_elements_by_css_selector("div[class='card h-100']")

        #finding only Blackberry mobile
        for product in products:
            productname = product.find_element_by_css_selector("div[class='card-body'] h4 a").text
            if productname == "Blackberry":
                product.find_element_by_css_selector("div[class='card-footer'] button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()


        time.sleep(4)
        self.driver.get_screenshot_as_file("abc1.png")

        #Page 2 - Checkout page
        #self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        a = Checkout(self.driver)
        a.Checkout_button().click()


        #Confirmation page
        #self.driver.find_element_by_css_selector("input[id='country']").send_keys("ind")
        b = Confirmation(self.driver)
        b.Confirmation4().send_keys("ind")

        #Explicit wait - moved to BaseClass1
        #wait = WebDriverWait(self.driver,10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.Linktext("India")

        #self.driver.find_element_by_link_text("India").click()
        #self.driver.find_element_by_css_selector("input[type='submit']").click()
        c = Confirmation(self.driver)
        c.Confirmation5().click()
        d = Confirmation(self.driver)
        d.Confirmation6().click()

        print (self.driver.find_element_by_css_selector("div[class*='alert-success']").text)
        assert "Success! Thank you!" in self.driver.find_element_by_css_selector("div[class*='alert-success']").text

        self.driver.get_screenshot_as_file("abc.png")

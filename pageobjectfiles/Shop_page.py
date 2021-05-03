from selenium.webdriver.common.by import By


class shoppage:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
    # driver.find_element_by_name("name").send_keys("abc")
    # driver.find_element_by_id("exampleCheck1").click()
    # driver.find_element_by_css_selector("input[name='name']").send_keys('abc')
    # Select class to handle selction in dropdown menu
    # select = Select(driver.find_element_by_id('exampleFormControlSelect1'))
    # select.select_by_visible_text('Female')
    # driver.find_element_by_xpath("//input[@type='submit']").click()
    #self.driver.find_element_by_id('exampleFormControlSelect1')

    shoppage1 = (By.NAME, "name")
    shoppage2 = (By.ID, "exampleCheck1")
    shoppage3 = (By.CSS_SELECTOR, "input[name='name']")
    shoppage4 = (By.XPATH, "//input[@type='submit']")
    shoppage9 = (By.ID, "exampleFormControlSelect1")

    def shoppage5(self):
        return self.driver.find_element(*shoppage.shoppage1)

    def shoppage6(self):
        return self.driver.find_element(*shoppage.shoppage2).click()

    def shoppage7(self):
        return self.driver.find_element(*shoppage.shoppage3)

    def shoppage8(self):
        return self.driver.find_element(*shoppage.shoppage4).click()

    def shoppage10(self):
        return self.driver.find_element(*shoppage.shoppage9)



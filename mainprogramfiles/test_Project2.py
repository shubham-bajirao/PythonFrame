import inspect
import logging
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from PytestFramework.pageobjectfiles.Checkout_page import Checkout
from PytestFramework.pageobjectfiles.Confirmation_page import Confirmation
from PytestFramework.Utilities2.BaseClass1 import BaseClass2
#@pytest.mark.usefixtures("setup")
from PytestFramework.pageobjectfiles.Shop_page import shoppage
from PytestFramework.Utilities2.ExcelData import Excelvalue

class TestOne1(BaseClass2):
    def test_begin(self, setparams):
        log = self.getLogger()
        #driver.find_element_by_name("name").send_keys("abc")
        #driver.find_element_by_id("exampleCheck1").click()
        #driver.find_element_by_css_selector("input[name='name']").send_keys('abc')
        a = shoppage(self.driver)
        a.shoppage5().send_keys(setparams[0])
        a.shoppage6()
        a.shoppage7().send_keys(setparams[1])

        # Select class to handle selction in dropdown menu
        #select = Select(a.shoppage10())
        #select.select_by_visible_text('Female')
        self.SelectOptionbytext(a.shoppage10(), setparams[2])

        #driver.find_element_by_xpath("//input[@type='submit']").click()
        log.info("Test Cases passed")
        a.shoppage8()
        self.driver.refresh()
        # Regular expressions for multiple classes scene class="alert alert-success alert-dismissible"

        #print(driver.find_element_by_css_selector("div[class*='alert-success']").text)
        #print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)
    #excel1 = Excelvalue()
    #exceldata = excel1.ExcelValues()
    #print(Excelvalue.ExcelValues())
    #@pytest.fixture(params=[('a','b','Male'),('x','y','Female')])
    @pytest.fixture(params=[(Excelvalue.ExcelValues()[0],Excelvalue.ExcelValues()[1],Excelvalue.ExcelValues()[2]), (Excelvalue.ExcelValues()[0],Excelvalue.ExcelValues()[1],Excelvalue.ExcelValues()[2])])
    def setparams(self, request):
        return request.param


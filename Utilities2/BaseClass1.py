#import pytest
import inspect
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.mark.usefixtures("setup")
class BaseClass2:
    def Linktext(self, text):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionbytext(self,locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

     #Code to integrate the screenshots with the report


from selenium import webdriver
import time
import pytest
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def test_cla(dr):
    print(dr.title)
    el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
    el2.click()


def test_cla1(wd):
    print(wd.title)
    el2 = wd.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
    el2.click()




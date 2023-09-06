from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait



dr = webdriver.Firefox()
dr.get("http://mobizon.ua/")
dr.set_window_size(1920, 1080)
el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
el2.click()
wait = WebDriverWait(dr, 20)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-login')))
element2 = wait.until(EC.title_contains('Сервіс СМС розсилок. SMS послуги для бізнесу — mobizon.ua'))

el3 = dr.find_element(By.CSS_SELECTOR, "input#email")
el3.clear()
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.clear()
el4.send_keys("")
element1.click()
time.sleep(5)

element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#sms-history-shortcut > div')))
element4.click()
wait.until(EC.presence_of_element_located((By.ID, "x-grid-rowbody-tr")))

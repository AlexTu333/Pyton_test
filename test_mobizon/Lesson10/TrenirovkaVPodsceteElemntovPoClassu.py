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
import random
from Lesson11SvoyCondition import all_sended_sms


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
el3.send_keys(".")
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.clear()
el4.send_keys("")
element1.click()
time.sleep(5)

element12 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#sms-history-shortcut > div'))) # Открыли историю СМС
element12.click()
old_sms_number = wait.until(EC.presence_of_element_located((By.ID, "gridview-1997-table")),
                            message="Ne mogu nayti element")   # Проверили статус элемента СМС в гриде


element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#main-menu-innerCt a.x-btn.x-unselectable.x-box-item.x-btn-simple-small.x-noicon.x-btn-noicon.x-btn-simple-small-noicon.x-over.x-btn-over.x-btn-simple-small-over.x-focus.x-btn-focus.x-btn-simple-small-focus > span > span > span.x-btn-icon-el')))
element4.click()
#Перешли в создание рассылки через боковое меню

el5 = dr.find_element(By.CSS_SELECTOR, "div#send-sms-body div > textarea")
el5.clear()
el5.send_keys("Ловим кнопку")
el6 = dr.find_element(By.CSS_SELECTOR, "div#send-sms-body td.x-form-item-body > textarea")
el6.clear()
el6.send_keys("")

element5 = wait.until(EC.element_to_be_clickable((By.ID, 'campaign-create-button-btnIconEl')))
dr.execute_script("arguments[0].scrollIntoView();", element5)
dr.execute_script("arguments[0].click();", element5)

dr.implicitly_wait(10)

element7 = wait.until(EC.element_to_be_clickable((By.ID, 'campaign-send-button-btnIconEl')))
time.sleep(5)
dr.execute_script("arguments[0].scrollIntoView();", element7)
dr.execute_script("arguments[0].click();", element7)
print(element7.location)
print(element7.size)

wait.until(EC.presence_of_element_located((By.ID, "gridview-1997-table")))

new_sms_number = old_sms_number + 1

el11 = wait.until(all_sended_sms((By.ID, 'campaign-send-button-btnIconEl'), new_sms_number),
                  message=f"V istorii SMS za iskomiy period doljno bit {new_sms_number}")
print(len(el11))

#Принцип верный, на Турбе работает - почему не работает на Мобизоне, нужно разобраться, посмотреть внимательно верстку, ИД и т.д.

#time.sleep(5)
#el10 = (By.CLASS_NAME, "aux-grid-sms-smartphone full-wrap")
#number_of_sms = wait.until(EC.visibility_of_all_elements_located(el10))  ## НЕ работает - нужно понять почему
#print(len(number_of_sms))






import button as button
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

dr = webdriver.Firefox()
dr.get("http://mobizon.ua/")
print(dr.title)
dr.set_window_size(1920, 1080)
# time.sleep(2)     # Но есть еще неявное ожидание dr.implicitly_wait(3) - ждет пока элемент появится, если задан find_elements, ждет пока хотя бы один элемент появится
el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
el2.click()
wait = WebDriverWait(dr, 20)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-login')))
# if not element1:
#    print('Time Out')
#wait2 = WebDriverWait(dr, 3)
element2 = wait.until(EC.title_contains('Сервіс СМС розсилок. SMS послуги для бізнесу — mobizon.ua'))

el3 = dr.find_element(By.CSS_SELECTOR, "input#email")
el3.clear()
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.clear()
el4.send_keys("")
element1.click()
time.sleep(5)


element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#send-sms-shortcut > div')))
element4.click()
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



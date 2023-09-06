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



a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = '[]{}()*"/,_-!?'
e = 'atur+'
j = '@mobizon.com'

all2 = a + c + d
lenght = 8
lenght2 = 1
password = "".join(random.SystemRandom().sample(all2, lenght))
password2 = "".join(random.SystemRandom().sample(b, lenght2))
final_password = password2 + password
print("Idet Generaciya Parolya")
time.sleep(3)
print("Parol Gotov")
print(final_password)
#input()
lenght3 = 4
cifra = "".join(random.SystemRandom().sample(c, lenght3))
all = e + cifra
email = all + j
print("Idet Generaciya email")
time.sleep(3)
print("Email Gotov")
print(email)


dr = webdriver.Firefox()
dr.get("http://mobizon.ua/")
print(dr.title)
dr.set_window_size(1920, 1080)
el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
el2.click()
wait = WebDriverWait(dr, 20)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-login')))
element2 = wait.until(EC.title_contains('Сервіс СМС розсилок. SMS послуги для бізнесу — mobizon.ua'))
el3 = dr.find_element(By.CSS_SELECTOR, "input#email")
el3.clear()
el3.send_keys(str(email))
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.clear()
el4.send_keys(str(final_password))
#element1.click()
#time.sleep(5)






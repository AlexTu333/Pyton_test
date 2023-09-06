import button as button
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

dr = webdriver.Firefox()
# dr.get("http://google.com/")
dr.get("http://mobizon.ua/")
print(dr.title)
# dr.refresh()
# dr.find_element_by_css_selector("p#btn-log > span.login-link")
# dr.find_element(By.ID, "btn-reg")
# el = dr.find_element_by_name("btnI")
# print(el)
# print(type(el))
#time.sleep(2)     # Но есть еще неявное ожидание dr.implicitly_wait(3) - ждет пока элемент появится, если задан find_elements, ждет пока хотя бы один элемент появится
el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
el2.click()
# el2.send_keys("addends")
# el2.send_keys(Keys.RETURN)
# print(el2)
# print(type(el2))
wait = WebDriverWait(dr, 3)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-login')), message="Knopka vhoda ne progruzilas")
#if not element1:
#    print('Time Out')
wait2 = WebDriverWait(dr, 3)
element2 = wait.until(EC.title_contains('Сервіс СМС розсилок. SMS послуги для бізнесу — mobizon.ua'))
#if not element2:
#    print('Ttile Change')
el3 = dr.find_element(By.CSS_SELECTOR, "input#email")
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.send_keys("")


def is_element_present(by, value):
    try:
        dr.find_element(by, value)
    except exceptions.NoSuchElementException:
        return False
    return True




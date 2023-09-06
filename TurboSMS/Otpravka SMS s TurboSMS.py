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
dr.get("https://turbosms.ua/")
print(dr.title)
#time.sleep(2)     # Но есть еще неявное ожидание dr.implicitly_wait(3) - ждет пока элемент появится, если задан find_elements, ждет пока хотя бы один элемент появится
el2 = dr.find_element(By.ID, "cookie_button")
el2.click()
time.sleep(2)
wait = WebDriverWait(dr, 5)
el2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.d-none.d-md-flex.align-items-center.justify-content-end > a#login_btn")))
dr.execute_script("arguments[0].scrollIntoView();", el2)
dr.execute_script("arguments[0].click();", el2)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#submit_auth')))
#if not element1:
#    print('Time Out')
#wait2 = WebDriverWait(dr, 3)
#element2 = wait.until(EC.title_contains('СМС рассылка'))
#if not element2:
#    print('Ttile Change')
el3 = dr.find_element(By.CSS_SELECTOR, "input#auth_login")
el3.clear()
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#auth_password")
el4.clear()
el4.send_keys("")
element1.click()
element2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#submenu-item-single-add')))
element2.click()
el5 = dr.find_element(By.CSS_SELECTOR, 'form[name="sendsms-single"] div.placeholder-container.form-line > label')
el5.click()
el6 = dr.find_element(By.CSS_SELECTOR, "#single_text")
el6.clear()
el6.send_keys("Я превзошел всех)) Мобизон и его сложные кнопки на очереди!!")
el6.click()
el7 = dr.find_element(By.CSS_SELECTOR, 'form[name="sendsms-single"] div.first-column.fl-left > div:nth-child(2) > label')
el7.click()
el8 = dr.find_element(By.CSS_SELECTOR, "textarea#number")
el8.clear()
el8.send_keys("380503565543")
el8.click()
el9 = dr.find_element(By.CSS_SELECTOR, "input#submitter_single")
el9.click()
element3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#submitter_single')))
element3.click()











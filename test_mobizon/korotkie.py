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
#time.sleep(2)     # Но есть еще неявное ожидание dr.implicitly_wait(3) - ждет пока элемент появится, если задан find_elements, ждет пока хотя бы один элемент появится
el2 = dr.find_element(By.CSS_SELECTOR, "p#btn-log > span.login-link")
el2.click()
wait = WebDriverWait(dr, 5)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-login')))
#if not element1:
#    print('Time Out')

element2 = wait.until(EC.title_contains('Сервіс СМС розсилок. SMS послуги для бізнесу — mobizon.ua'))
#if not element2:
#    print('Ttile Change')
el3 = dr.find_element(By.CSS_SELECTOR, "input#email")
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#password")
el4.send_keys("")
element1.click()
time.sleep(5)
#wait3 = WebDriverWait(dr, 5)
#element3 = wait.until(EC.element_to_be_clickable((By.ID, 'button-1117-btnIconEl')))
#element3.click()

element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#short-links-shortcut > div')))
element4.click()

element5 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div/div['
                                                            '2]/div/div/a[1]/span/span/span[2]')))
dr.execute_script("arguments[0].scrollIntoView();", element5)
dr.execute_script("arguments[0].click();", element5)

element4 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div[4]/div['
                                                            '2]/div/div[1]/span/div/table[2]/tbody/tr/td[2]/input')))
element4.send_keys("https://www.youtube.com/")

element7 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#short-links a.x-btn.x-box-item.x-toolbar-item.x-btn-primary-small')))
print(element7.tag_name)
dr.execute_script("arguments[0].scrollIntoView();", element7)
dr.execute_script("arguments[0].click();", element7)

#el7 = dr.find_element(By.CSS_SELECTOR, "div#short-links a.x-btn.x-box-item.x-toolbar-item.x-btn-primary-small")
#el7.click()









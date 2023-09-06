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


dr = webdriver.Firefox()
dr.get("https://www.google.com//")
print(dr.title)
dr.set_window_size(1920, 1080)
el4 = dr.find_element(By.CSS_SELECTOR, "textarea#APjFqb")
el4.send_keys(Keys.CONTROL, "a")
time.sleep(1)
el4.send_keys(Keys.DELETE)
el4.send_keys("Робокоп")
el4.send_keys(Keys.ENTER)
WebDriverWait(dr, 10).until(EC.staleness_of(el4))
el5 = dr.find_element(By.CSS_SELECTOR, "textarea#APjFqb")
el5.send_keys(Keys.CONTROL, "a")
time.sleep(1)
el5.send_keys(Keys.DELETE)
el5.send_keys("Lala")
el5.send_keys(Keys.ENTER)
#el5.screenshot('/home/aleksey/Desktop/lalalal1.png')
#dr.save_screenshot('/home/aleksey/Desktop/lalalal1.png')
print(el5.tag_name)
#time.sleep(5)
#dr.quit()


#dr1 = webdriver.Firefox()
#dr1.get("https://www.google.com//")






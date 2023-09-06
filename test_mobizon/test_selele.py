import button as button
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import staleness_of


dr = webdriver.Firefox()
dr.get("https://www.google.com//")
print(dr.title)
el4 = dr.find_element(By.CSS_SELECTOR, "textarea#APjFqb")
el4.send_keys("Ivan Sherbak")
el5 = dr.find_element(By.CSS_SELECTOR, 'div.FPdoLc.lJ9FBc > center > input[name="btnK"]')
#el6 = dr.find_element(By.CSS_SELECTOR, "div.L3eUgb > div.o3j99.LLD4me.yr19Zb.LS8OJ")
#el6.click()
#wait = WebDriverWait(dr, 3)
#element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.FPdoLc.lJ9FBc > center > input[name="btnK"]')))
el5.click()
WebDriverWait(dr, 20).until(EC.staleness_of(el4))
#dr.switch_to.window("https://www.google.com//")
el6 = dr.find_element(By.CSS_SELECTOR, "textarea#APjFqb")
el6.send_keys(Keys.CONTROL, "a")
time.sleep(1)
el6.send_keys(Keys.DELETE)
el6.send_keys("AAAAAAAAAA")
el6.send_keys(Keys.ENTER)



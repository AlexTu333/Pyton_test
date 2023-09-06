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
wait = WebDriverWait(dr, 5)
el2 = dr.find_element(By.ID, "cookie_button")
el2.click()
time.sleep(5)
el2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.d-none.d-md-flex.align-items-center.justify-content-end > a#login_btn")))
dr.execute_script("arguments[0].scrollIntoView();", el2)
dr.execute_script("arguments[0].click();", el2)
element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#submit_auth')))
el3 = dr.find_element(By.CSS_SELECTOR, "input#auth_login")
el3.clear()
el3.send_keys("")
el4 = dr.find_element(By.CSS_SELECTOR, "input#auth_password")
el4.clear()
el4.send_keys("")
element1.click()
element4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#submenu-item-sended')))
element4.click()
#old_sms_number = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'no-row-click')))
dr.find_elements(By.CLASS_NAME, 'no-row-click')
rrr = len(dr.find_elements(By.CLASS_NAME, 'no-row-click'))
print(rrr)
new_sms_number = rrr + 2
time.sleep(5)

element2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#submenu-item-single-add')))
element2.click()
el5 = dr.find_element(By.CSS_SELECTOR, 'form[name="sendsms-single"] div.placeholder-container.form-line > label')
time.sleep(2)
el5.click()
el6 = dr.find_element(By.CSS_SELECTOR, "#single_text")
el6.clear()
el6.send_keys("TEST TEST")
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
time.sleep(2)
element3.click()


def all_sended_sms(locator, number):

    def _predicate(dr):
        allsms = dr.find_elements(*locator)
        if len(allsms) == number:
            return allsms

    return _predicate

el11 = wait.until(all_sended_sms((By.CLASS_NAME, 'no-row-click'), new_sms_number),
                  message=f"V istorii SMS za iskomiy period doljno bit {new_sms_number}")
print(len(el11))



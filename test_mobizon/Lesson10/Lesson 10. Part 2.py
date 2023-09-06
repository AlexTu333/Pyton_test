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


# dr = webdriver.Firefox()
# dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
# el1 = dr.find_element(By.CSS_SELECTOR, '#options')
# print(el1.tag_name)
# el1.click()
# dropdown = Select(el1)
# dropdown.Select_by_index(3)

dr = webdriver.Firefox()
dr.get("https://mobizon.ua/")
wait = WebDriverWait(dr, 7)
el1 = dr.find_element(By.CSS_SELECTOR, 'li:nth-child(6) > a')
actions = webdriver.ActionChains(dr)
actions.move_to_element(el1)
actions.click(el1)
actions.perform()

#Так запускается гугл, все вроде бы работает, только команды типа print(menu.text) не выполняются
#service = Service(executable_path='/home/aleksey/Desktop/ChromeDrivers/114.0.5735.90/chromedriver')
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
#wd = webdriver.Chrome(service=service, options=options)
#time.sleep(5)
wd = webdriver.Firefox()
wd.get("https://python.org/")
wd.implicitly_wait(5)

menu = wd.find_element(By.ID, 'downloads')
submenu = menu.find_elements(By.TAG_NAME, 'li')[1]
action = webdriver.ActionChains(wd)
action.move_to_element(menu)
action.pause(3)
action.click(submenu)
action.perform()
print(menu.text)



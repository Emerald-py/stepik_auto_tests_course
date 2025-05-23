from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
import math
import time


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	WDW(browser, 13).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
	browser.find_element(By.ID, "book").click()
	res = calc(int(browser.find_element(By.ID, "input_value").text))
	browser.find_element(By.ID, "answer").send_keys(res)
	browser.find_element(By.ID, "solve").click()
finally:
	time.sleep(7)
	browser.quit()

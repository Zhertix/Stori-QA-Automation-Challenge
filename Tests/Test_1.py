import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

##Test 1: Suggestion Class Example

def test_autocomplete():
        try:
            print('Test 1: Suggestion Class Example')
            suggestion_input = driver.find_element(By.XPATH, '//*[@id="autocomplete"]')
            suggestion_input.send_keys("Me")
            time.sleep(3)
            sugg_list = driver.find_elements(By.CLASS_NAME, 'ui-menu-item')
            sugg_list[5].click()
            time.sleep(3)
            print('Test 1: Success')
        except:
            print('Test 1: Fail')
            return(suggestion_input,sugg_list)
        driver.close()
test_autocomplete()

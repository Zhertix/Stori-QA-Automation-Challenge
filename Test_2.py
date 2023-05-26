import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


##Test 2: Dropdown Example

def test_autocomplete():
    try:
        print('Test 2: Drowp Down')
        select = Select(driver.find_element(By.XPATH, '//*[@id="dropdown-class-example"]'))
        time.sleep(2)
        select.select_by_value('option2')
        time.sleep(2)
        opSelect = driver.find_element(By.XPATH, '//*[@id="dropdown-class-example"]/option[3]')
        print(opSelect.text)
        print('--- Option 2 Selected')
        if(opSelect.text ==  'Option2'):
            print('---- PASS')
        else:
            print('---- FAIL')
        select.select_by_value('option3')
        time.sleep(5)
        opSelect = driver.find_element(By.XPATH, '//*[@id="dropdown-class-example"]/option[4]')
        print(opSelect.text)
        print('--- Option 3 Selected')
        if(opSelect.text ==  'Option3'):
            print('---- Pass')
        else:
            print('---- Fail')
    except:
        print('Test 2: Fail')
        return(select)
    
    driver.close()
    
test_autocomplete()
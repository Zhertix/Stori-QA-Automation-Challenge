from asyncio import wait
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


input_name = driver.find_element(By.XPATH, '//*[@id="name"]')
button1 = driver.find_element(By.ID, 'alertbtn')
button2 = driver.find_element(By.ID, 'confirmbtn')
alertText = 'Hello Stori Card, share this practice page and share your knowledge'
confirmText = 'Hello Stori Card, Are you sure you want to confirm?'
    ##print text alert button
def test_autocomplete(): 
    try:  
        print('Test 5: Alert Example')
        input_name.send_keys('Stori Card') 
        button1.click()
        time.sleep(2)
        alert = driver.switch_to.alert 
        text = alert.text
        print('Text obtained: '+ text)
        print('Status: ')
        if(text == alertText):
            print('--- PASS')
        else:
            print('--- FAIL')
        alert.accept()
        time.sleep(3)

        ## print text confirm button alert
        input_name.send_keys('Stori Card') 
        button2.click()
        confirm = driver.switch_to.alert 
        text = confirm.text
        print('Text obtained: '+ text)
        print('Status: ')
        if(text == confirmText):
            print('--- PASS')
        else:
            print('--- FAIL')
        alert.accept()
        time.sleep(3)
    except:
        print('Test 5: Fail')
        return( input_name,button1,button2)
    
    driver.close()

    
test_autocomplete()




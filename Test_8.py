import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Store iframe web element
iframe = driver.find_element(By.XPATH,'//*[@id="courses-iframe"]')

    # switch to selected iframe
def test_autocomplete():
    try:
        print('Test 8: IFrame')
        list_odd = [1,3,5]
        list_a = []
        list_b = []
        iframe = driver.find_element(By.XPATH,'//*[@id="courses-iframe"]')
        driver.switch_to.frame(iframe)
        text = driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]').text
        for x in list_odd:
            list_a.append(driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div/div/div[1]/ul/li[' + str(x) + ']').text)
        for y in list_odd:
            list_b.append(driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[' + str(y) + ']').text)
        print('Test 8: IFrame: ' + text)
        print('List Odd Texts: ')
        for b in list_a:
            print('-'+b)
        for c in list_b:
            print('-'+c)
    except:
        print('Test 8: IFrame')
        print('--- Fail')
        driver.close()
        return(list_odd,list_a,list_b,iframe,text)

    driver.close()
    
test_autocomplete()

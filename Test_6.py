import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

##Test x: Tables
def test_autocomplete():
    try:
        print('Test 6: Tables')
        
        pricesTableXpath = ['//*[@id="product"]/tbody/tr[2]/td[3]', '//*[@id="product"]/tbody/tr[3]/td[3]', '//*[@id="product"]/tbody/tr[4]/td[3]', '//*[@id="product"]/tbody/tr[5]/td[3]', '//*[@id="product"]/tbody/tr[6]/td[3]', '//*[@id="product"]/tbody/tr[7]/td[3]', '//*[@id="product"]/tbody/tr[8]/td[3]', '//*[@id="product"]/tbody/tr[9]/td[3]', '//*[@id="product"]/tbody/tr[10]/td[3]', '//*[@id="product"]/tbody/tr[11]/td[3]']
        nameTableXpath = ['//*[@id="product"]/tbody/tr[2]/td[2]', '//*[@id="product"]/tbody/tr[3]/td[2]', '//*[@id="product"]/tbody/tr[4]/td[2]', '//*[@id="product"]/tbody/tr[5]/td[2]', '//*[@id="product"]/tbody/tr[6]/td[2]', '//*[@id="product"]/tbody/tr[7]/td[2]', '//*[@id="product"]/tbody/tr[8]/td[2]', '//*[@id="product"]/tbody/tr[9]/td[2]', '//*[@id="product"]/tbody/tr[10]/td[2]', '//*[@id="product"]/tbody/tr[11]/td[2]']
        count = 0
        index = 0
        names = []
    ## Courses price
        for x in pricesTableXpath:
            index += 1
            if driver.find_element(By.XPATH, x).text == '25':
                count += 1
                names.append(driver.find_element(By.XPATH, nameTableXpath[index - 1]).text)
    ##Course names 
        print('Test 6: Found: ' + str(count) + ' courses that are $25.')
        print('Named Courses:')
        for a in names:
            print('-' + a)
    except:
        print('Test 6: Fail')
        return(pricesTableXpath,nameTableXpath,count,index, names)
    
    driver.close()

    
test_autocomplete()
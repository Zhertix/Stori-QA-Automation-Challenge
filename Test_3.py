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


##Test 3: Switch window and verify text
def test_autocomplete():
    try:
        print('Test 3: Switch Window')
        page1 = driver.current_window_handle
        tabButton = driver.find_element(By.XPATH, '//*[@id="openwindow"]')
        tabButton.click()
        page2 = driver.window_handles
        for w in page2:
            if(w!=page2):
                driver.switch_to.window(w)

        print("Child window title: " + driver.title)

        text_label = driver.find_element(By.XPATH, '//*[@id="category-part"]/div/div/div/div[1]/div/h2')
        label = text_label.get_attribute('textContent')
        print(label)

        if label == 'Best platform to learn Software and Automation Testing':
            print('FAIL')
        else:
            print('PASS')
            
        time.sleep(4)
    except:
        print('Test 3: Fail')   
        return(page1,tabButton,page2,text_label,label)

    driver.close()
    driver.switch_to.window(page1)
    driver.close()


test_autocomplete()

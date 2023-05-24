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

##Test 4: Switch tab and verify text
def test_autocomplete():
    try:
        print('Test 4: Switch Tab')
        page1 = driver.current_window_handle
        tabButton = driver.find_element(By.ID, "opentab")
        tabButton.click()
        page2 = driver.window_handles 

        ##print(page2)
        for w in page2:
            if(w!=page2):
                driver.switch_to.window(w)       
        print("Child window title: " + driver.title)
        text_label = driver.find_element(By.XPATH, '//*[@id="header-part"]/div[2]/div/div/div[2]/div/div[2]/a')
        label = text_label.get_attribute('textContent')
        print(label)
        time.sleep(5)
        ##No scroll needed since the button appears on the top of the page :v

        driver.save_screenshot('./Test4.png')

        time.sleep(2)

        driver.switch_to.window(page1)

        time.sleep(5)
    except:
        print('Test 4: Fail')
        return(page1,tabButton,page2,text_label,label)
    
    driver.close()

    
test_autocomplete()

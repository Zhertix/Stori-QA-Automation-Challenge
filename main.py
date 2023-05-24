import sys
import time
import Test_1
import Test_2
import Test_3
import Test_4
import Test_5
import Test_6
import Test_8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = sys.argv[2]

match browser:
    case "Chrome":
        driver = webdriver.Chrome()
    case "Firefox":
        driver = webdriver.Firefox()
    case "Edge":
        driver = webdriver.Edge()
    case "Safari":
        driver = webdriver.Safari()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


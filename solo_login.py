# Script for automating login to a webpage (in this case, solo) with selenium. Replace usernameStr and passwordStr with your credentials.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome()
browser.get(('https://devsolo.liveu.tv'))
username = browser.find_element_by_id('txtUsername')
username.send_keys(usernameStr)
password = browser.find_element_by_id('txtPassword')
password.send_keys(passwordStr)

signInButton = WebDriverWait(browser, 5).until(browser.find_element_by_id('btnLogin')
signInButton.click()

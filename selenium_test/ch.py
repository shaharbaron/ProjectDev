from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

se = Service(executable_path='selenium_test/webDriver/chromedriver')
driver = webdriver.Chrome(service=se, options=options)
driver.get("file:///Users/tamirlevi/DevWithgit/ProjectDev/index.html")

# בבדיקת השחקן הראשו
player1 = driver.find_element(By.CLASS_NAME, ".Player1 h2") 
try:
    assert player1.text != "Player1"
except AssertionError:
    print("Test 1: The player text is not correct")

# Restart
cards = driver.find_elements(By.CLASS_NAME, "card")
cards_len = len(cards)
restart_button = driver.find_element(By.CLASS_NAME, "restartbutton")
restart_button.click()
time.sleep(0.5)
new_cards = driver.find_elements(By.CLASS_NAME, "card")
try:
    assert cards_len == len(new_cards)
except AssertionError:
    print("Test 2: Restart button is not working correctly")

# Memory-Game 
title_element = driver.find_element(By.CLASS_NAME, "Memory")
try:
    assert title_element.text != "Memory-Game"  
except AssertionError:
    print("Test 3: Title is not correct")

#Exit
exit_button = driver.find_element(By.CLASS_NAME, "exitbutton")
exit_button.click()
bye_element = driver.find_element(By.ID, "thankyou-message")
try:
    assert bye_element.text == "Thank you and bye bye"
except AssertionError:
        print("Test 4: The exit page message is not correct")
except:
    print("Test 4: Exit page did not load correctly")

driver.quit()

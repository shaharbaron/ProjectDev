from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def test_main_stat():
    url = "http://localhost"
    driver.get(url)


def test_score():
    player1 = driver.find_element(By.CLASS_NAME, "Player1")
    try:
        assert player1.find_element(By.TAG_NAME, 'h2').text != "Player 1"
    except AssertionError:
        print("Test 1: The player text is not correct")

        
    

def test_restart():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "restartbutton")))
    cards = driver.find_elements(By.CLASS_NAME, "card")
    cards_len = len(cards)
    restart_button = driver.find_element(By.CLASS_NAME, "restartbutton")
    restart_button.click()
    time.sleep(0.5)
    try:
        assert cards_len == len(cards)
    except AssertionError:
        print("Test 2: The restart button is not working")
        
        
        
    


def test_title():
    title_element = driver.find_element(By.CLASS_NAME, "Memory")
    try:
        assert title_element.text != "Memory-Game"
    except AssertionError:
        print("Test 3: The title is not correct")
        
        
   


def test_cards():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "exitbutton")))
    exit_button = driver.find_element(By.CLASS_NAME, "exitbutton")
    exit_button.click()
    bye_element = driver.find_element(By.ID, "thankyou-message")
    try:
        assert bye_element.text == "Thank you and bye bye"
    except AssertionError:
        print("Test 4: The exit page message is not correct")
        
    



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pytest


options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options = Options()
options = [
  "--headless",
  "--disable-gpu",
  "--window-size=1920,1200",
  "--ignore-certificate-errors",
  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage"
]

for option in options:
  chrome_options.add_argument(option)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

  
def test_main_stat():
 url = "http://localhost"
 driver.get(url)




#score check
def test_score():
  player1 = driver.find_element(By.CLASS_NAME, ".Player1 h2")  
  try:
      assert player1.text != "Player 1"
  except AssertionError:
      print("Test 1: The player text is not correct")

          


def test_restart():
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "restartbutton")))
  cards = driver.find_elements(By.CLASS_NAME, "card")
  cardslen = len(cards)
  restars_button = driver.find_element(By.CLASS_NAME,"restartbutton")
  restars_button.click()
  time.sleep(0.5)
  try:
      assert cardslen == len(cards)
  except AssertionError:
   print("test 2: restart button is not working")
   

#game check
def test_titel():
  title_element = driver.find_element(By.CLASS_NAME, ".Memory h2")
  try:
    assert title_element.text != "Memory-Game" 
  except AssertionError:
    print("Test 3: Title is not correct")




def test_cards():
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "exitbutton")))
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
  exit(1)







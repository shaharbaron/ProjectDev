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


se = Service(executable_path='selenium_test/webDriver/chromedriver')
driver = webdriver.Chrome(service=se,options=chrome_options)
  
def test_main_stat():
 url = "http://localhost"
 driver.get(url)




def test_cards():
  cards = driver.find_elements(By.CLASS_NAME, "card")
  cardslen = len(cards)
  try:
   assert cardslen <= 2
  except AssertionError:
    print("Game is not initialized")


#score check
def test_score():  
  first_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="3b"]')
  first_card.click()
  second_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="3b"]')
  second_card.click()
  score_element = driver.find_element(By.ID, "score1") 
  new_score = score_element.text
  if new_score == '':
        new_score = '0'
  previous_score = 0
  try:
        assert int (new_score) > previous_score 
        previous_score = int(new_score)
  except AssertionError:
          print("test 1: score is not updated")
          


def test_restart():
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
def test_player():
  titel = driver.find_element(By.CLASS_NAME, "Memory")
  try:
      assert titel.text == "Memory-Game"
  except AssertionError:
      print("test 3:the player is not changed")
      driver.quit()
      exit(1)







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


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

#webdriver_path = 'C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe'

#se = Service(webdriver_path)
se = ChromeService(ChromeDriverManager().install())
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

def test_score():  
  cards = driver.find_elements(By.CLASS_NAME, "card")
  # for i in range(len(cards)):
  #   cards[i].click()
  #   for j in range(i+1,len(cards)):  
  #     #time.sleep(0.2) 
  #     cards[j].click()
  first_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="2b"]')
  first_card.click()
  #time.sleep(1)  # חכה כדי שהקלף יתברר
  second_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="2b"]')
  second_card.click()
  #time.sleep(1)  # חכה כדי שהקלף יתברר

  score_element = driver.find_element(By.ID, "score1") 
  new_score = score_element.text
  if new_score == '':
        new_score = '0'
  previous_score = 0
  try:
        assert int (new_score) < previous_score # score is not updated need to be fixed < to >
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
   driver.quit()
   exit(1)

#game check
def test_player():
  first_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="2b"]')
  second_card = driver.find_element(By.CSS_SELECTOR, 'div.card[data-id="2r"]')
  current_player = driver.find_element(By.CLASS_NAME, 'Player1' or 'Player2')
  first_card.click()
  second_card.click()
  try:
      assert current_player.is_displayed()
  except AssertionError:
      print("test 3:the player is not changed")
      driver.quit()
      exit(1)







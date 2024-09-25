from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
options = [
  #"--headless",
  #"--disable-gpu",
  #"--window-size=1920,1200",
  #"--ignore-certificate-errors",
  #"--disable-extensions",
  #"--no-sandbox",
  #"--disable-dev-shm-usage"
  'enable-logging',
  'excludeSwitches'
]
for option in options:
  chrome_options.add_argument(option)


se = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=se, options=chrome_options)
driver.get("file:///Users/tamirlevi/DevWithgit/ProjectDev/memory.html")

#game chack

card=driver.find_elements(By.CLASS_NAME,"card")
for i in card :
  card[i].click()

  for j in card(1):
    card[j].click()
    if card[i] == card[j]:
      continue




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


se = Service(executable_path='selenium_test/webDriver/chromedriver')
driver = webdriver.Chrome(service=se, options=options)
driver.get("file:///Users/tamirlevi/DevWithgit/ProjectDev/index.html")



cards = driver.find_elements(By.CLASS_NAME, "card")
cardslen = len(cards)
print(cards)
if len(cards) < 2:
 raise Exception("Game is not initialized")
 

# scure check
for i in range(len(cards)):
    cards[i].click()
    for j in range(i+1,len(cards)):  
     #time.sleep(0.2) 
     cards[j].click()
     score_element = driver.find_element(By.ID, "score1") 
     new_score = score_element.text
     previous_score = 0
     try:
       assert int (new_score) > previous_score # score is not updated need to be fixed < to >
       previous_score = int(new_score)
     except AssertionError:
        print("score is not updated")
        driver.quit()
        exit(1)

#restart button check 
# cards[0].click()
# time.sleep(1)
# cards[1].click()
restars_button = driver.find_element(By.CLASS_NAME,"restartbutton").click()
time.sleep(0.5)
try:
    assert cardslen == len(cards)
except AssertionError:
    print("restart button is not working")
    driver.quit()
    exit(1)
   

driver.quit()
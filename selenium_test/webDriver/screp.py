from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#remove windows warning messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#change path to where your have it!
se = Service(executable_path='selenium_test/webDriver/chromedriver')
driver = webdriver.Chrome(service=se,options=options)
driver.get("https://www.shopsite.com/ready-to-buy.html")


free_btn = driver.find_elements(By.CLASS_NAME,"btn")
print(free_btn)
free_btn[1].click()

driver.quit()



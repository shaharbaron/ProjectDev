from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#remove windows warning messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#change path to where your have it!
se = Service(executable_path='webDriver/chromedriver')
driver = webdriver.Chrome(service=se,options=options)
driver.get("https://www.shopsite.com/ready-to-buy.html")

# username_box = driver.find_element(By.ID,"username")
# username_box.click()
# username_box.send_keys("abcd")
# email_box = driver.find_element(By.ID,"useremail")
# email_box.click()
# email_box.send_keys("tt@gmail.com")
# agree_box = driver.find_element(By.ID,"shareemail").click()
# #btn =driver.find_element(By.CSS_SELECTOR,".btn").click()
# purchases =driver.find_element(By.CSS_SELECTOR,"#bs-example-navbar-collapse-1 > ul > li:nth-child(3) > a").click() 
# partners = driver.find_element(By.XPATH,"//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/a").click()
# partners = driver.find_element(By.XPATH,"//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/ul/li[1]/a").click()
free_btn=driver.find_elements(By.CLASS_NAME,"btn")
print(free_btn)
free_btn[0].click()
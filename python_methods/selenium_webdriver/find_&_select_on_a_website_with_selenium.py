from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#path where chrome driver is installed
chrome_driver_path = "S:\Devops\Downloading files(temp)\chrome_driver_folder\chromedriver.exe"
#
# service = Service(chrome_driver_path)
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#get(url=the website we want to scrape)
# driver.get("https://www.ajio.com/fossil-es3838-chronograph-watch-with-leather-strap/p/4915035850_multi")
# driver.implicitly_wait(30)
#1
# price = driver.find_element(By.CLASS_NAME, "prod-sp")
# print(price.text)

driver.get("https://www.python.org/")
#2
search_bar = driver.find_element(By.NAME, "q")
#3
print(search_bar.tag_name)
#4(which helps to print the value of an attribute)
print(search_bar.get_attribute("placeholder"))
id = driver.find_element(By.ID, "submit")
print(id.text)
#5(when no attribute like class, id is available)
doc = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(doc.text)

#6(xpath is the most helpful way if it's nested many times)
bug_fix = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_fix.text)

#7.find all elements we can use "driver.find_elements(......)"

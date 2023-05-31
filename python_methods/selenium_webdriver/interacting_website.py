from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path  = "S:\Devops\Downloading files(temp)\chrome_driver_folder\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

##finding elements with css selector which helps to narrow down to the path
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

article_count.click()

#Helps to locate anchor tag (hyperlink)
all_portals = driver.find_element(By.LINK_TEXT, "View history")

##Helps to click on anchor tags / Buttons
all_portals.click()

#Helps to input the values or keys by importing keys class

search = driver.find_element(By.NAME, "search")
search.send_keys("Python") ##Helps to input value
search.send_keys(Keys.ENTER) ##helps to use keyboard keys to perfom an action


Example:
=======
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fname")
fname.send_keys("suresh")
fname = driver.find_element(By.NAME, "lname")
fname.send_keys("kumar")
fname = driver.find_element(By.NAME, "email")
fname.send_keys("mail@email.com")

signup = driver.find_element(By.CSS_SELECTOR, "form button")
signup.click()

#Shows the success button if it's correct

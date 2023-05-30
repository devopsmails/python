from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "S:\Devops\Downloading files(temp)\chrome_driver_folder\chromedriver.exe"
#
# service = Service(chrome_driver_path)
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name":event_names[n].text
    }

print(events)
{0: {'time': '2023-05-30', 'name': 'An Introduction to Pyro'},
 1: {'time': '2023-06-02', 'name': 'PyData London 2023'},
 2: {'time': '2023-06-03', 'name': 'PyDay La Paz 2023'}, 
 3: {'time': '2023-06-17', 'name': 'Django Girls Xai-Xai'},
 4: {'time': '2023-06-20', 'name': 'Building Micro Tech Communities Around Python Programming Language (June 20 - July 30)'}}

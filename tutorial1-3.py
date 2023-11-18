# # Selenium Tutorial
# # https://sites.google.com/chromium.org/driver/?pli=1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.python.org")

search = driver.find_element(by=By.ID, value="id-search-field")
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

# Find all the titles on page
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )

    h3List = element.find_elements(by=By.TAG_NAME, value="h3")
    for eachH3 in h3List:
      aTag = eachH3.find_element(by=By.TAG_NAME, value="a")
      # print(aTag.text)
      
except:
    print("list-recent-events not found")
    driver.quit()


# Navigation
bugsInPython235Link = element.find_element(by=By.LINK_TEXT, value="Bugs in Python 2.3.5")
bugsInPython235Link.click()

try:
    elementbugsInPython235Title = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Bugs in Python 2.3.5']"))
    )

    platformReportsLink = driver.find_element(by=By.LINK_TEXT, value="777867")
    platformReportsLink.click()

except:
    print("Bugs in Python 2.3.5 in title not found")
    driver.quit()


# Navigation back
driver.back()
driver.back()
driver.back()
driver.forward()
driver.forward()


time.sleep(5)
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait until lang select is loaded
try:
    langSelect = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    langSelect.click()
      
except:
    print("langSelect not found")
    driver.quit()

# Wait until bigCookie is clickable
try:
    bigCookie = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "bigCookie"))
    )

    numCookies = driver.find_elements(by=By.XPATH, value="//div[@id='cookies']")
    items = [driver.find_element(by=By.ID, value="productPrice" + str(i)) for i in range(1, -1, -1)]

    cookieClickAction = ActionChains(driver=driver)
    upgrade_actions = ActionChains(driver=driver)
    
    for i in range(5000):
      cookieClickAction.move_to_element(bigCookie)
      cookieClickAction.click(bigCookie)
      cookieClickAction.perform()
      # bigCookie.click()
      numCookiesCount = int(numCookies[0].text.split(" ")[0])
      # print(numCookiesCount)
      for item in items:
          value = int(item.text)
          if value <= numCookiesCount:
              # item.click()              
              upgrade_actions.move_to_element(item)
              upgrade_actions.click()
              upgrade_actions.perform()
      
except:
    print("bigCookie not found")
    driver.quit()





# items = [driver.find_element(by=By.ID, value="productPrice" + str(i)) for i in range(1,-1,-1)]





#driver.quit()


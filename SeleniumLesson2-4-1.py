from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)
try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "button")
finally:
    browser.quit()
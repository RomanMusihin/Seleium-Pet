from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'Test.txt')           # добавляем к этому пути имя файла 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Roman")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Surname")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("mail@gmail.com")
    send_file = browser.find_element(By.ID, 'file').send_keys(file_path)
    time.sleep(1)
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
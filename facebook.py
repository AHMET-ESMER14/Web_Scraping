from selenium import webdriver
from selenium.webdriver.common.by import By
import time

a = webdriver.Chrome()

a.get("https://tr-tr.facebook.com/")

a.fullscreen_window()
time.sleep(1)

login = a.find_element(By.ID,"email")
password = a.find_element(By.ID,"pass")

login.send_keys("")     # enter email
password.send_keys("")  # enter password

b = a.find_element(By.CSS_SELECTOR,"button[type='submit']")
b.click()
a.fullscreen_window()
a.fullscreen_window()
time.sleep(4)
a.fullscreen_window()
a.fullscreen_window()


a.get("https://www.facebook.com/profile")
a.fullscreen_window()
time.sleep(2)


a.get("https://www.facebook.com/media/")
a.fullscreen_window()
time.sleep(10)
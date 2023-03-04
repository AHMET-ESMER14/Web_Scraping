from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("")    # driver path

browser.get("https://www.linkedin.com/")

browser.fullscreen_window()
time.sleep(3)

login = browser.find_element_by_xpath("/html/body/nav/a[3]")
login.click()
time.sleep(3)

email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("")         # enter email
password.send_keys("")      # enter password

login_button = browser.find_element_by_css_selector("#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button")
login_button.click()
time.sleep(3)

search_bar = browser.find_element_by_xpath("//*[@id='ember29']/input")
search_bar.send_keys("")  # enter search words
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

browser.quit()
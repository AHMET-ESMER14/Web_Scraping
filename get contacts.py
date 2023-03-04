from selenium import webdriver
import time

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


contacts = browser.find_element_by_xpath("//*[@id='mynetwork-tab-icon']")
contacts.click()
time.sleep(3)

contact_button = browser.find_element_by_class_name("mn-community-summary__entity-info")
contact_button.click()
time.sleep(3)

for i in range(1,5):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

followers = browser.find_elements_by_class_name("mn-connection-card__details")
fallowerList = []

for i in followers:
    fallowerList.append(i.text)

with open ("follower.txt","w+",encoding = "UTF-8") as file:
    for i in fallowerList:
        file.write(i + "/n")

time.sleep(5)
browser.quit()
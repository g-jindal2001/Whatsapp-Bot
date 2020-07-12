from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, sys

def new_chat(user_name):
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()

    new_user = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    time.sleep(1)

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()

    except NoSuchElementException:
        print('Given User "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\INTEL\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')
chrome_browser = webdriver.Chrome(executable_path='C:\\Users\\INTEL\\Desktop\\Driver\\chromedriver', options=options)
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

user_name_list = ['Test', 'Mom']

for user_name in user_name_list:

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()

    except NoSuchElementException:
        new_chat(user_name)

    # Typing message into message box
    message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
    message_box.send_keys('Hey, I am your whatsapp bot')

    # Click on send button
    message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    message_box.click()
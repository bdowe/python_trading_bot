import os
import sys
sys.path.append('../')

import requests
from time import sleep
from splinter import Browser
from selenium import webdriver

from configs.config import \
    client_id, \
    redirect_uri, \
    td_username, \
    td_pass, \
    td_sec_q1_a, \
    td_sec_q2_a, \
    td_sec_q3_a, \
    td_sec_q4_a

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

method = 'GET'
url = "https://auth.tdameritrade.com/auth"

payload = {
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "client_id": client_id + "@AMER.OAUTHAP"
}

built_url = requests.Request(method, url, params=payload).prepare().url

browser = Browser('chrome', options=options)

browser.visit(built_url)
sleep(1)

browser.find_by_id("username0").fill(td_username)
browser.find_by_id("password").fill(td_pass)
browser.find_by_id("accept").first.click()
sleep(1)

browser.find_by_text("Can't get the text message?").first.click()
browser.find_by_name("init_secretquestion").first.click()
sleep(1)

browser.find_by_id("secretquestion0").fill(td_sec_q2_a)
browser.driver.find_elements_by_class_name("checkboxContainer")[0].click()
browser.find_by_id("accept").first.click()
sleep(1)

browser.find_by_id("accept").first.click()
sleep(1)

browser.find_by_id("details-button").first.click()
sleep(1)
browser.find_by_id("proceed-link").first.click()
sleep(3)

new_url = browser.url
print(url)



# sleep(3)
# browser.driver.close()
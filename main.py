import time

import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Access Strapi API

URL = "https://app.sli.do/event/ou9jq3kt/live/polls"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(URL)

WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.XPATH , "/html/body/div[3]/div/div/div/div/div/div[1]/sda-live/div/sda-polls/div/div[1]/sda-poll/div[2]/form/sda-poll-question/div[2]/poll-question-input/div/div[1]/div/div[7]/label/div/div"))).click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[1]/sda-live/div/sda-polls/div/div[1]/sda-poll/div[2]/form/div/div[1]/div/button[2]").click() 

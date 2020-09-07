
from time import sleep
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from parsel import Selector

import pandas as pd

# Source: 
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html).replace("\n", "").strip()
    return cleantext

wait_time = 6
name_matches = []
collected_names = []
experiences = []

# Read from CSV
df = pd.read_csv("linkedins.csv")
names = df["names"]

# Iniciar navegador Chrome
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://linkedin.com")

# Fazer login
WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, "nav__button-secondary"))).click()
WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("YOUR LINKEDIN EMAIL HERE")
browser.find_element_by_id("password").send_keys("YOUR LINKEDIN PASSWORD HERE")
browser.find_element_by_id("password").send_keys(Keys.ENTER)

for name in names:
    
    # Pesquisar
    WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/form/div/div/div/div/div[1]/div/input'))).send_keys(name)
    browser.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input").send_keys(Keys.ENTER)

    # Selecionar perfil
    WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-result__result-link.search-result__result-link'))).click()

    # Coletar informacoes
    sleep(wait_time)
    sel = Selector(text=browser.page_source)

    beg = sel.css("div.ph5.pb5")
    exp = sel.css("section.pv-profile-section.experience-section.ember-view")

    collected_name = cleanhtml( beg.css("li.inline.t-24.t-black.t-normal.break-words").get() )
    exps = exp.css("h3.t-bold.t-black").getall()
    experience = ""
    # Remove HTML tags, "\n" and trailing spaces from experiences
    for i in range(len(exps)):
        exps[i]  = cleanhtml( exps[i] )
        experience = experience + exps[i] + " "
    
    name_matches.append( bool(collected_name.find(name)) )
    collected_names.append(collected_name)
    experiences.append(experience)

df["matched"] = name_matches
df["name_found"] = collected_names
df["experience"] = experiences
df.to_csv("linkedin_infos.csv")
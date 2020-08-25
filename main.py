
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from parsel import Selector

wait_time = 5
# For testing
name = ""

# Iniciar navegador Chrome
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://linkedin.com")

# Fazer login
WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, "nav__button-secondary"))).click()
WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("YOUR EMAIL HERE")
browser.find_element_by_id("password").send_keys("YOUR PASSWORD HERE")
browser.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()

# Pesquisar
sleep(wait_time)
browser.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input").send_keys(name)
browser.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input").send_keys(Keys.ENTER)

# Selecionar perfil
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[1]/a'))).click()

# Coletar informações
sleep(wait_time)
sel = Selector(text=browser.page_source)

browser.quit()

collected_name = sel.css("li.inline.t-24.t-black.t-normal.break-words").extract_first()
experience = sel.css("span.text-align-left.ml2.t-14.t-black.t-bold.full-width.lt-line-clamp.lt-line-clamp--multi-line.ember-view").extract_first()

print(collected_name.find(name))
print(experience)
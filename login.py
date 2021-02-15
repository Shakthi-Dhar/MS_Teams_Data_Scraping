# importing all required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# defining the path of your selenium web-driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

########################################################################################################################
# enter mail and password and team name you are searching for here
email = ""
password = ""
team_name = ""
########################################################################################################################

url = "https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=6eef1e9d-d07e-48b1-b03a-8c50d62d5a52&client-request-id=42dfa2d2-fc11-4285-97ad-7ef5b06f974c&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=ad9ecad9-b21c-4a56-9a46-af00bd177178&domain_hint=&sso_reload=true"
driver.get(url)

wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))
email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)

work = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="aadTile"]')))
work.click()

pass_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]')))
pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)

sign_in = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
sign_in.click()

driver.implicitly_wait(20)

team_select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInputField"]')))
team_select.send_keys(team_name)
driver.execute_script("arguments[0].aria-activedescendant='autosuggest-id-1')",team_select)
team_select.click()

# driver.close()

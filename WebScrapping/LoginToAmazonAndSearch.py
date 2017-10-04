import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

print("Opening website ..");

browser = webdriver.Firefox()
browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&switch_account=')

login_user = browser.find_element_by_id("ap_email")
login_user.clear()
login_user.send_keys("b.hgt@gmail.com")

login_pass = browser.find_element_by_id("ap_password")
login_pass.clear()
login_pass.send_keys("2014@")

login_button = browser.find_element_by_id("signInSubmit")
login_button.submit()

print("Login success ...")

delay = 5 # seconds
try:
    search_field = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

search_field.send_keys("redmi 4 32 gb")
search_field.submit()

# http://selenium-python.readthedocs.io/locating-elements.html
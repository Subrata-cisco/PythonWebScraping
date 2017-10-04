import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def wait(delay,bytype,tag):
    try:
        return_tag = WebDriverWait(browser, delay).until(EC.presence_of_element_located((bytype, tag)))
    except TimeoutException:
        print("Loading took too much time!")
    return return_tag


webSite = "https://www.uscis.gov/"
print("Opening website : {} ".format(webSite));
browser = webdriver.Firefox()
browser.get(webSite)

continue_link = browser.find_element_by_link_text('Check your Case Status')
continue_link.click()

receipt_number_field = wait(3,By.ID,"receipt_number")

r_number = "EAC1714450340"
print("Checking status for : {}".format(r_number))
receipt_number_field.send_keys(r_number)
receipt_number_field.submit()

elem = wait(3,By.CSS_SELECTOR,"div.rows.text-center")
h1tag = elem.find_element_by_tag_name("h1")

print("Status is : {}".format(h1tag.text))

browser.quit()
import selenium
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def wait(delay, bytype, tag, forasset):
    return_tag = None
    try:
        return_tag = WebDriverWait(browser, delay).until(EC.presence_of_element_located((bytype, tag)))
    except TimeoutException:
        print("Buy option not available for :", forasset)
    return return_tag


binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
binary.add_command_line_options('-headless')

webSite = "http://www.moneycontrol.com/india/stockpricequote/"
print("Opening website : {} ".format(webSite));
browser = webdriver.Firefox(firefox_binary=binary)
browser.get(webSite)

table = wait(5, By.CSS_SELECTOR, ".pcq_tbl.MT10", "Main-Page")
listOfLinks = list()

for row in table.find_elements_by_xpath(".//tr"):
    for col in row.find_elements(By.TAG_NAME, "td"):
        listOfLinks.append(col.text)

print("Total stock :", len(listOfLinks))

allStocks = dict()
count = 0;

for col in listOfLinks:
    if count == len(listOfLinks) + 1:
        break
    count = count + 1

    try:
        if count != 1:
            table = wait(5, By.CSS_SELECTOR, ".pcq_tbl.MT10", col)

        table.find_element_by_link_text(col).click()
        percentage = wait(5, By.XPATH, "//span[@class='pl_txt']", col)

        if percentage is not None:
            buy_text = wait(5, By.XPATH, "//span[@class='pl_txt wrd']", col)
            if buy_text.text == 'BUY':
                if allStocks.get(percentage.text) is not None:
                    allStocks[percentage.text] += "[" + (col + "]")
                else:
                    allStocks[percentage.text] = ("[" + col + "]")
                    # print("Stock : {} , Advice : {} , Percentage : {}".format(col,buy_text.text,percentage.text))
        browser.back()

    except Exception:
        print("Could not finish processing all..")

for key, value in allStocks.items():
    print("Percentage : {} , Stocks : {}".format(key, value))

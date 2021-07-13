from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

def scrape(email_list):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://mxtoolbox.com/")
    assert "MX Lookup Tool" in driver.title
    provider_list = []
    for email in email_list:
        provider_list.append(search_provider(driver,email))
    print(provider_list)

def search_provider(driver,email):
    try: search_box = driver.find_element_by_xpath('//input[@class="tools_lookup_textbox form-control"]')
    except: search_box = driver.find_element_by_xpath('//input[@class="tools_lookup_textbox form-control supertool-input"]')
    search_box.clear()
    search_box.send_keys(email)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)
    #driver.find_element_by_xpath('//a[@id="btnAction3"]').click()
    #time.sleep(10)
    alert = driver.find_element_by_xpath('//pre[@class="alert"]').text
    return(alert.split('"')[1])

if __name__ == '__main__':
    scrape(['algartelecom.com.br','navesmuller.com.br'])
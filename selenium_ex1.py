from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com")
browser.find_element('q').send_keys('Test')

time.sleep(5)

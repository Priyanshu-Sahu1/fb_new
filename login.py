import scrapy
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import sys
sys.path.append(r'C:\Users\dell\Downloads\Change_Original\quotes\quotes\spiders')
import pandas as pd
import parameter
import quotes_spider
def login():
        quotes_spider.driver.get("https://wwww.facebook.com/")
        # target username
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        print(username)
        # enter username and password
        username.clear()
        username.send_keys(parameter.Facebook_username)
        password.clear()
        # use your username and password
        password.send_keys(parameter.Facebook_password)
        # target the login button and click it
        time.sleep(2)
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        # We are logged in!
        print("Logged in")
        # program to parse user name who posted comment
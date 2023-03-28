import sys
sys.path.append('src')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

API_TOKEN = os.getenv('API_TOKEN')

def parser_config():
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')
    
    s = Service("chromedriver/chromedriver")
    driver = webdriver.Chrome(service=s, options=options)
    
    return driver
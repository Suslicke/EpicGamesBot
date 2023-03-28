import sys
import time
sys.path.append('src')

from datetime import datetime, timedelta
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from db.queries import db_queries
from cache_worker.cache_worker import cache_worker
from config import parser_config

import game_details


def main():
    driver = parser_config()
    url = 'https://www.epicgames.com/store'
    lang = "en-US"
    # lang_ru = "ru"
    driver.get(f"{url}/{lang}/")
    free_games_section = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/en-US/free-games"]'))
    )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    parse_free_games(soup, url)
    driver.quit()
    time.sleep(10)
    game_details.main()
    
    
def parse_free_games(soup, url):
    game_cards = soup.find("a", {"href": "/en-US/free-games"}).find_previous("div").find_next('section').find_next('div')

    time_now = datetime.now()
    for game_card in game_cards:
        game_title = game_card.find("div", {"data-testid": "offer-title-info-title"}).find_next('div').contents[0]
        
        game_status = game_card.find("div", {"data-testid": "offer-card-image-landscape"}).find_next_sibling("div").find("span").contents[0]
        game_status_datetime = game_card.find("span", {"data-testid": "offer-title-info-subtitle"}).find("span").find_all("time")
        
        active_time = datetime.strptime(game_status_datetime[0].get('datetime'), "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(hours=3)
        
        soon_time = datetime.strptime(game_status_datetime[1].get('datetime'), "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(hours=3)
        active_time_end = (active_time - time_now)
        
        game_image_url = game_card.find("img")["src"]
        
        game_url = url + game_card.find("a")["href"]
        
        new = db_queries.create_game(game_title, game_image_url, game_status, game_url, active_time)
        
        cache_worker.set_new_game_time(str(active_time))
        cache_worker.set_new_game(new)


if __name__ == "__main__":
    schedule.every().day.at("00:00:00").do(main)
    # schedule.every().day.at("12:30:45").do(main)
    # schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)

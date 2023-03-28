import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from config import parser_config

from db.queries import db_queries

def main():
    games = db_queries.get_last_game()
    
    for game in games:
        driver = parser_config()
        driver.get(game.game_url)
        free_games_page = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="pdp-title"]'))
            )
        soup = BeautifulSoup(driver.page_source, "html.parser")
        parse_game_detail(soup)
        time.sleep(15)
        driver.quit()
    
        
        
def parse_game_detail(soup):
    
    title = soup.find("span", {"data-testid": "pdp-title"}).contents[0]
    metadata = soup.find_all("div", {"data-testid": "about-metadata-layout-column"})
    short_desc = soup.find("div", {"data-testid": "about-metadata-layout-column"}).find_previous("div").find_previous("div").find_previous("div").contents[0]

    #MB later
    # long_desc = soup.find("div", {"data-testid": "about-long-description"})
    # print(long_desc)

    specifications = soup.find("span", string="Specifications").find_next("div")

    for spec in specifications:
        platforms = spec.find("div", {"role": "tablist"}).find_all('span')
        platform_list = [platform.contents[0] for platform in platforms]
        
        # MINIMUM
        minimum = spec.find('div', {"role": "tabpanel"}).find('span', string="Minimum")
        
        try:
            min_os = minimum.find_next("div").find_next("div").find("span").find_next("span").contents[0]
        except:
            min_os = "No information"
        
        try:
            if minimum.find_next("div").find_next("div").find_next("span", string="Processor"):
                min_processor = minimum.find_next("div").find_next("div").find_next("span", string="Processor").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="CPU"):
                min_processor = minimum.find_next("div").find_next("div").find_next("span", string="CPU").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Windows Processor"):
                min_processor = minimum.find_next("div").find_next("div").find_next("span", string="Windows Processor").find_next("span").contents[0]
            else:
                min_processor = "No information"    
        except:
            min_processor = "No information"
        
        try:
            if minimum.find_next("div").find_next("div").find_next("span", string="Memory"):
                min_memory = minimum.find_next("div").find_next("div").find_next("span", string="Memory").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Windows Memory"):
                min_memory = minimum.find_next("div").find_next("div").find_next("span", string="Windows Memory").find_next("span").contents[0]
        except:
            min_memory = "No information"
        
        try:
            if minimum.find_next("div").find_next("div").find_next("span", string="Video Card"):
                min_video = minimum.find_next("div").find_next("div").find_next("span", string="Video Card").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Graphics"):
                min_video = minimum.find_next("div").find_next("div").find_next("span", string="Graphics").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="GPU"):
                min_video = minimum.find_next("div").find_next("div").find_next("span", string="GPU").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Windows Graphics"):
                min_video = minimum.find_next("div").find_next("div").find_next("span", string="Windows Graphics").find_next("span").contents[0]
            else:
                min_video = "No information"
        except:
            min_video = "No information"
        
        try:
            if minimum.find_next("div").find_next("div").find_next("span", string="HDD Space"):
                min_space = minimum.find_next("div").find_next("div").find_next("span", string="Storage").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Storage"):
                min_space = minimum.find_next("div").find_next("div").find_next("span", string="Storage").find_next("span").contents[0]
            elif minimum.find_next("div").find_next("div").find_next("span", string="Windows Storage"):
                min_space = minimum.find_next("div").find_next("div").find_next("span", string="Windows Storage").find_next("span").contents[0]
            else:
                min_space = "No information"    
        except:
            min_space = "No information"
            
        
        # RECOMENDED
        rec = spec.find('div', {"role": "tabpanel"}).find('span', string="Recommended")
        
        try:
            rec_os = rec.find_next("div").find_next("div").find("span").find_next("span").find_next("span").find_next("span").contents[0]
        except:
            rec_os = "No information"
        
        try:
            if rec.find_next("div").find_next("div").find_next("span", string="Processor"):
                rec_processor = rec.find_next("div").find_next("div").find_next("span", string="Processor").find_next("span", string="Processor").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="CPU"):
                rec_processor = rec.find_next("div").find_next("div").find_next("span", string="CPU").find_next("span", string="CPU").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Windows Processor"):
                rec_processor = rec.find_next("div").find_next("div").find_next("span", string="Windows Processor").find_next("span", string="Windows Processor").find_next("span").contents[0]
            else:
                rec_processor = "No information"    
        except:
            rec_processor = "No information"
        
        try:
            if rec.find_next("div").find_next("div").find_next("span", string="Windows Memory"):
                rec_memory = rec.find_next("div").find_next("div").find_next("span", string="Windows Memory").find_next("span", string="Windows Memory").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Memory"):
                rec_memory = rec.find_next("div").find_next("div").find_next("span", string="Memory").find_next("span", string="Memory").find_next("span").contents[0]
        except:
            rec_memory = "No information"
        
        try:
            if rec.find_next("div").find_next("div").find_next("span", string="Video Card"):
                rec_video = rec.find_next("div").find_next("div").find_next("span", string="Video Card").find_next("span", string="Video Card").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Graphics"):
                rec_video = rec.find_next("div").find_next("div").find_next("span", string="Graphics").find_next("span", string="Graphics").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="GPU"):
                rec_video = rec.find_next("div").find_next("div").find_next("span", string="GPU").find_next("span", string="GPU").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Windows Graphics"):
                rec_video = rec.find_next("div").find_next("div").find_next("span", string="Windows Graphics").find_next("span", string="Windows Graphics").find_next("span").contents[0]
            else:
                rec_video = "No information"
        except:
            rec_video = "No information"
        
        try:
            if rec.find_next("div").find_next("div").find_next("span", string="HDD Space"):
                rec_space = rec.find_next("div").find_next("div").find_next("span", string="HDD Space").find_next("span", string="HDD Space").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Storage"):
                rec_space = rec.find_next("div").find_next("div").find_next("span", string="Storage").find_next("span", string="Storage").find_next("span").contents[0]
            elif rec.find_next("div").find_next("div").find_next("span", string="Windows Storage"):
                rec_space = rec.find_next("div").find_next("div").find_next("span", string="Windows Storage").find_next("span", string="Windows Storage").find_next("span").contents[0]
            else:
                rec_space = "No information"    
        except:
            rec_space = "No information"
        

    for data in metadata:
        what_data = data.find("div").find("span").contents[0]
        datas = data.find("ul").find_all("li")
        
        clean_data = [clean_data.find_next("span").find_next("span").contents[0] for clean_data in datas]
        
        # print(what_data) #Genres/Features
        if what_data == "Genres":
            genres = ' '.join(clean_data)
        else:
            features = ' '.join(clean_data)
    
    
    game = db_queries.get_game_by_title(title)
    db_queries.create_game_detail(title, short_desc, genres, features)
    
    game_id = game.id
    
    game_detail_id = db_queries.get_game_detail(game_id).id
    
    types = ['Minimum', 'Recommended']
    
    for type in types:
        db_queries.create_game_detail_specifications(game_detail_id, type, rec_os, rec_processor, rec_video, rec_memory, rec_space)
    

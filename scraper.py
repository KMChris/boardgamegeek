from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
from tqdm import tqdm
from random import random
import pandas as pd
import os

def read_games():
    columns = ['name', 'year', 'description',
        'min_players', 'max_players', 'min_play_time',
        'max_play_time', 'min_age', 'complexity',
        'alternate_names', 'designers', 'artists',
        'publishers', 'ratings', 'avg_rating',
        'std_rating', 'ratings_1', 'ratings_2',
        'ratings_3', 'ratings_4', 'ratings_5',
        'ratings_6', 'ratings_7', 'ratings_8',
        'ratings_9', 'ratings_10', 'comments',
        'fans', 'page_views', 'plays', 'plays_month',
        'owners', 'prev_owned', 'for_trade',
        'want_in_trade', 'wishlist']
    try:
        df = pd.read_csv('games.csv')
        eval_columns = ['alternate_names', 'designers', 'artists', 'publishers']
        df[eval_columns] = df[eval_columns].map(eval)
    except FileNotFoundError:
        df = pd.DataFrame(columns=columns)
    return df

class Scraper:
    def __init__(self, pages=100):
        options = ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.links = self.get_links(pages=pages)
        self.setup()

    def setup(self):
        load_dotenv()
        self.driver.get("https://boardgamegeek.com/browse/boardgame")
        
        # Allow cookies on first visit
        self.driver.find_element(By.CLASS_NAME, "fc-cta-consent").click()
        
        # Login
        username = os.getenv('USER')
        password = os.getenv('PASS')
        self.driver.find_element(By.CSS_SELECTOR, "button[login-required]").click()
        self.driver.find_element(By.ID, "inputUsername").send_keys(username)
        self.driver.find_element(By.ID, "inputPassword").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def get_links(self, pages=100):
        links = []
        try:
            with open('links.txt', 'r') as f:
                links = f.readlines()
            if len(links) >= pages * 100:
                return links
            else:
                offset = len(links) // 100
        except FileNotFoundError:
            offset = 0
        
        for page in tqdm(range(offset + 1, pages + 1)):
            while True:
                self.driver.get(f'https://boardgamegeek.com/browse/boardgame/page/{page}?sort=numvoters&sortdir=desc')
                sleep(random())
                
                # Find all the links on the page
                anchors = self.driver.find_elements(By.CLASS_NAME, 'primary')
                if anchors:
                    links += [link.get_attribute('href') for link in anchors]
                    break

                # If the page is empty, wait and try again
                sleep(10)
        
        with open('links.txt', 'w') as f:
            for link in links:
                f.write(link + "\n")
        return links

    def get_property(self, selector, attribute='text', convert=None):
        try:
            if attribute == 'text':
                result = self.driver.find_element(By.CSS_SELECTOR, selector).text
            else:
                result = self.driver.find_element(By.CSS_SELECTOR, selector).get_attribute(attribute)
            
            if convert:
                return convert(result)
            return result
        except:
            return None

    def get_game(self, link):
        self.driver.get(link + '/stats')
        sleep(random() * 8 + 2) # Sleep between 2 and 10 seconds
        game = {}

        # Basic info
        game['name'] = self.get_property('span[itemprop="name"]')
        game['year'] = self.get_property('span.game-year', convert=lambda x: x.strip('()'))
        game['description'] = self.get_property('span[itemprop="description"]')
        game['min_players'] = self.get_property('[itemprop="numberOfPlayers"] meta[itemprop="minValue"]', 'content')
        game['max_players'] = self.get_property('[itemprop="numberOfPlayers"] meta[itemprop="maxValue"]', 'content')
        play_time = self.get_property('ul.gameplay > li:nth-child(2) > p > span > span', convert=lambda x: x.split('–'))
        game['min_play_time'] = play_time[0] if play_time else None
        game['max_play_time'] = play_time[-1] if play_time else None
        game['min_age'] = self.get_property('span[itemprop="suggestedMinAge"]')
        game['complexity'] = self.get_property('[item-poll-button="boardgameweight"] > span')

        # Credits
        alternate_names = self.driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="alternateName"]')
        game['alternate_names'] = [name.text for name in alternate_names]
        designers = self.driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="creator"]')
        game['designers'] = [name.text for name in designers]
        artists = self.driver.find_elements(By.CSS_SELECTOR, 'div.game-header-credits > ng-include > div > ul > li:nth-child(3) > popup-list > span.ng-scope > a > span')
        game['artists'] = [name.text for name in artists]
        publishers = self.driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="publisher"]')
        game['publishers'] = [name.text for name in publishers]

        # Stats
        titles = {
            'Avg. Rating': 'avg_rating',
            'No. of Ratings': 'ratings',
            'Std. Deviation': 'std_rating',
            'Comments': 'comments',
            'Fans': 'fans',
            'Page Views': 'page_views',
            'All Time Plays': 'plays',
            'This Month': 'plays_month',
            'Own': 'owners',
            'Prev. Owned': 'prev_owned',
            'For Trade': 'for_trade',
            'Want In Trade': 'want_in_trade',
            'Wishlist': 'wishlist'
        }
        for elem in self.driver.find_elements(By.CLASS_NAME, 'outline-item'):
            title = self.get_property(elem, '.outline-item-title')
            if title in titles:
                game[titles[title]] = self.get_property(elem, '.outline-item-description',
                                                convert=lambda x: x.split('\n')[0].replace(',', ''))

        # Rank distribution
        ratings = self.driver.find_elements(By.CSS_SELECTOR, 'ratings-stats-graph > div > div > div:nth-child(1) > div > div > table > tbody > tr > td:nth-child(2)')
        for i, elem in enumerate(ratings):
            try:
                game['ratings_' + str(i+1)] = elem.get_attribute('innerHTML').replace(',', '')
            except:
                game['ratings_' + str(i+1)] = None
        return game

    def get_games(self, games=100):
        df = read_games()
        offset = len(df)
        for link in tqdm(self.links[offset:offset+games]):
            df.loc[len(df)] = self.get_game(link)
            if len(df) % 10 == 0 or len(df) == offset + games:
                df.to_csv('games.csv', index=False)

    def __del__(self):
        self.quit()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--pages', type=int, default=100)
    parser.add_argument('-g', '--games', type=int, default=10000)
    args = parser.parse_args()

    scraper = Scraper(pages=args.pages)
    scraper.get_games(limit=args.games)

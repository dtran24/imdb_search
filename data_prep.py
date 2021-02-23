from bs4 import BeautifulSoup
import requests

from time import sleep
from random import randint
import json

from utils import list_to_file, file_to_list

DATA_STORE_FP = 'data_store.json'

class IMDBDataPrep:
    """ For scraping IMDB and creating file that stores the data scraped """
    def __init__(self,
                 movie_data_fp='movie_data.txt',
                 movie_names_fp='movie_names.txt',
                 data_store_fp=DATA_STORE_FP):
        self.movie_data_fp = movie_data_fp
        self.movie_names_fp = movie_names_fp
        self.data_store_fp = data_store_fp

    def scrape_movie_data(self, start, end, incr):
        """
        Scrapes the top 1000 movies by rating
        Source: https://www.kaggle.com/akdagmelih/web-scraper-imdb-movies
        """
        names = []
        data = []

        headers = {'Accept-Language': 'en-US, en;q=0.5'}
        for i in range(start, end+1, incr):
            print(f'Scraping movies {i} through {i + incr - 1}')
            # Getting the contents from the each url
            url = 'https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc&start=' + str(
                i) + '&ref_=adv_nxt'
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Aiming the part of the html we want to get the information from
            movie_div = soup.find_all('div', class_='lister-item mode-simple')

            # Controlling the loop’s rate by pausing the execution of the loop for a specified amount of time
            # Waiting time between requests for a number between 2-10 seconds
            # for limit on requests per minute
            sleep(randint(2, 10))

            for container in movie_div:
                # Getting name
                name = container.span.a.text
                names.append(name)

                # Getting line with director and actors/actresses
                span = None
                for i, child in enumerate(container.span.children):
                    if i == 3:
                        span = child
                        break
                data.append(span['title'])

        print('Writing movie names and data')
        list_to_file(data, self.movie_data_fp)
        list_to_file(names, self.movie_names_fp)

    def create_data_store(self):
        movie_names = file_to_list(self.movie_names_fp)
        movie_data = file_to_list(self.movie_data_fp)

        movie2keywords = {}

        for i in range(len(movie_names)):
            name = movie_names[i].lower()
            data = movie_data[i]

            parts = data.split(',')
            dir_part = parts[0]
            dir_end_idx = dir_part.find('(dir.)') - 1
            director = dir_part[:dir_end_idx].lower()

            actor1 = parts[1].strip().lower()

            actor2 = parts[2].strip().lower()

            keywords = []
            keywords.extend(name.split())
            keywords.extend(director.split())
            keywords.extend(actor1.split())
            keywords.extend(actor2.split())

            keywords_dict = {k: 0 for k in keywords}
            movie2keywords[name] = keywords_dict

        with open(self.data_store_fp, 'w') as f:
            f.write(json.dumps(movie2keywords))


if __name__ == '__main__':
    # Example usage
    dp = IMDBDataPrep()
    dp.scrape_movie_data(1, 100, 50)
    print('Scraped')
    dp.create_data_store()
    print('Made data store')

import json
import time

import requests
from bs4 import BeautifulSoup

from scraper_metacritic.parse_data_page import get_soup_general_data

start_time = time.time()

session = requests.Session()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (HTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


def http_to_soup(url: str):
    """
    Helper function
    :param url: url
    :return: bs4 soup
    """
    response = session.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_last_page(url: str) -> int:
    """
    :param url: на вход принимаем начальную страничку (или любую) и находим номер последнюю
    :return: возвращаем номер последней странички
    """
    link = url + '0'
    get_ses_url = http_to_soup(link)
    page = get_ses_url.find_all('a', {"class": "page_num"})[-1]
    return int(page.text)


def get_details_link(url: str) -> str:
    """
    Helper function
    :param url: приходит часть внутренней ссылки из html кода типа '/game/<platform>/<name>/critic-reviews
    :return: возвращается ссылка на игру https://www.metacritic.com/game/<platform>/<name>/
    """
    return 'https://www.metacritic.com' + url.replace('critic-reviews', '')


def details_game_data(details_link: str) -> dict:
    """
    Helper function for game data by link game
    :return: dict with data
    """
    soup = http_to_soup(details_link)
    data = get_soup_general_data(soup)
    return data


def metacritic_web_scrapper(url: str, page: int) -> list[dict]:
    """
    Helper function to create data by games for write to json
    :return: dict with data
    """
    link = url + str(page)
    soup = http_to_soup(link)
    games = soup.findAll('tr')
    data = []
    for i in range(0, len(games), 2):
        details_link = get_details_link(games[i].find('a', {'class': 'metascore_anchor'})['href'])
        game_data = details_game_data(details_link)
        data.append(game_data)
    return data


def writing_to_json_data(url: str):
    """
    Creating json with uniq_data for metacritic_web_scrapper function
    """
    last_page = get_last_page(url)
    for page in range(0, last_page):
        with open(f'metacritic_data_json_game/games_from_page{page}.json', 'a') as file:
            game_link = metacritic_web_scrapper(url, page)
            json.dump(game_link, file)


def main():
    url = 'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&view=detailed&page='
    writing_to_json_data(url)
    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")


if __name__ == '__main__':
    main()

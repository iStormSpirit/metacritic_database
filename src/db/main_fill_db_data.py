import asyncio
import json
import os

import aiosqlite
import dateutil.parser

path_db = '../games_roulette.db'
path_to_uniq_data = '../../scraper_metacritic/metacritic_data_json_game/uniq_data.json'
path_to_folder = '../../scraper_metacritic/metacritic_data_json_game'
path_to_data = '../../scraper_metacritic/metacritic_data_json_game/games_from_page0.json'


async def autofill_db_tables(platform: str, name: str):
    """
    This function fill database tables: developer, genre, platform, publisher
    :param platform:
    :param name:
    """
    async with aiosqlite.connect(path_db) as db:
        await db.execute(f"INSERT INTO `{platform}` (name) VALUES (?)", [name])
        await db.commit()


async def writen_tables():
    """
    Reading data from json to be written for autofill_db_tables function
    """
    with open(f'{path_to_data}/uniq_data.json', 'r') as file:
        res = json.load(file)
        for table_name in res:
            print(table_name)
            for name in res[table_name]:
                await autofill_db_tables(str(table_name), name)
            print(f'{table_name} done')


async def autofill_db_game_table(name: str, details_link: str,
                                 release_date, num_players: str, meta_score: int,
                                 users_score: float, image: str, descriptions: str):
    """
    This function fill database game table
    :param name:
    :param details_link:
    :param release_date:
    :param num_players:
    :param meta_score:
    :param users_score:
    :param image:
    :param descriptions:
    """

    async with aiosqlite.connect(path_db) as db:
        release_date = dateutil.parser.parse(release_date).date()
        await db.execute("""INSERT INTO game
        (name, detail_link, release_date, num_players,
        meta_score, user_score, image_link, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                         [name, details_link,
                          release_date, num_players, meta_score,
                          users_score, image, descriptions])
        await db.commit()


async def writen_table_game():
    """
    Reading data from json to be written for autofill_db_game_table function
    """
    num_files = len([f for f in os.listdir(path_to_folder)
                     if os.path.isfile(os.path.join(path_to_folder, f))]) - 1
    # num_files = 1
    # for page in range(76, 202):
    for page in range(0, num_files):
        with open(f'{path_to_folder}/games_from_page{page}.json', 'r') as file:
            res = json.load(file)
            for item in res:
                name = item['name']
                details_link = item['details_link']
                release_date = item['release_date']
                # num_players = item['num_players']
                meta_score = item['meta_score']
                users_score = item['users_score']
                # image = ['image']
                # descriptions = ['descriptions']
                print(name, details_link, release_date, meta_score, users_score)
                # print(name, details_link, release_date, num_players, meta_score, users_score, image, descriptions)
                # await autofill_db_tables(name, details_link, release_date, num_players, meta_score, users_score, image, descriptions)



async def main():
    # await writen_tables()
    await writen_table_game()
#     TODO: writen_table_game доделать с проверкой

if __name__ == '__main__':
    asyncio.run(main())

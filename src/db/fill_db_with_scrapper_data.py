import asyncio
import json
import os

import aiosqlite
import dateutil.parser

path_db = '../metacritic.db'
path_to_uniq_data = '../../scraper_metacritic/metacritic_data_json_game/uniq_data.json'
path_to_folder = '../../scraper_metacritic/metacritic_data_json_game'


class MyError(Exception):
    pass


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
    with open(path_to_uniq_data, 'r') as file:
        res = json.load(file)
        for table_name in res:
            for name in res[table_name]:
                await autofill_db_tables(str(table_name), name)


async def autofill_db_game_table(name: str, details_link: str,
                                 release_date, num_players: str, meta_score: int,
                                 users_score: float, image: str, descriptions: str):
    """
    This function fill database game table
    :param name: str
    :param details_link: str
    :param release_date: str (auto converting to datetime.date())
    :param num_players: str
    :param meta_score: int
    :param users_score: float
    :param image: str - like link to .png
    :param descriptions: str
    """

    async with aiosqlite.connect(path_db) as db:
        try:
            release_date = dateutil.parser.parse(release_date).date()
        except MyError:
            release_date = dateutil.parser.parse('2024-01-01').date()
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
    for page in range(0, int(num_files)):
        print(page)
        with open(f'{path_to_folder}/games_from_page{page}.json', 'r') as file:
            res = json.load(file)
            for item in res:
                name = item['name']
                details_link = item['details_link']
                release_date = item['release_date']
                try:
                    num_players = item['num_players']
                except MyError:
                    num_players = None
                meta_score = item['meta_score']
                users_score = item['users_score']
                image = item['image']
                descriptions = item['descriptions']
                await autofill_db_game_table(name=name, details_link=details_link, release_date=release_date,
                                             num_players=str(num_players), meta_score=meta_score,
                                             users_score=users_score, image=str(image), descriptions=str(descriptions))


async def main():
    await writen_tables()
    await writen_table_game()


if __name__ == '__main__':
    asyncio.run(main())

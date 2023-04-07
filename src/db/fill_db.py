import asyncio
from sqlite3 import Error

import aiosqlite

path_db = '../games_roulette.db'


class Database():
    @staticmethod
    async def ConnectDatabase():
        try:
            db = await aiosqlite.connect(path_db)
            await db.commit()
            return db
        except Error:
            print(Error)

    @staticmethod
    async def insert_to_databese(db, values):
        c = await db.cursor()
        await c.execute('INSERT INTO publisher (id, name)'
                        'VALUES (?, ?)', values)
        await db.commit()


async def insert_to_db(values):
    async with aiosqlite.connect(path_db) as db:
        await db.execute("INSERT INTO publisher (id, name)"
                         "VALUES (?, ?)", values)
        await db.commit()
        return db


async def select_from_db():
    async with aiosqlite.connect(path_db) as db:
        # await db.execute("SELECT (?) FROM (?)", values)
        # await db.execute_fetchall("SELECT * FROM publisher")
        c = await db.cursor()
        await c.execute("SELECT * FROM publisher")
        records = await c.fetchall()
        return records
        # for i in records:
        #     print(i)
        # return db


async def main():
    # values = (125, 'as536zxcasd')
    # res = await insert_to_db(values)
    values = ('*', 'publisher')
    # table = 'publisher'
    res = await select_from_db()
    for i in res:
        print(i)
    # print(res)
    # database = await Database.ConnectDatabase()
    # values = [85, 'vjkf']
    # await asyncio.gather(Database.insert_to_databese(database, values))
    # await database.close()


if __name__ == '__main__':
    asyncio.run(main())

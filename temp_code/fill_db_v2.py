import asyncio

import aiosqlite

path_db = '../games_roulette.db'


async def insert_to_db(values):
    async with aiosqlite.connect(path_db) as db:
        await db.execute("INSERT INTO (?), (id, name)"
                         "VALUES (?, ?)", values)
        await db.commit()
        return db


async def select_all_from_db(table, choice='*', ):
    async with aiosqlite.connect(path_db) as db:
        c = await db.cursor()
        await c.execute(f"SELECT {choice} FROM {table}")
        records = await c.fetchall()
        return records


async def selected(table, values):
    async with aiosqlite.connect(path_db) as db:
        c = await db.cursor()
        await c.execute(f"SELECT * FROM {table} WHERE id = {values}")
        records = await c.fetchone()
        return records


async def autofill_db(platfrom: str, id: int, name: str):
    async with aiosqlite.connect(path_db) as db:
        await db.execute(f"INSERT INTO `{platfrom}` (id, name) VALUES (?, ?)", [id, name])
        await db.commit()


async def main():
    pass


if __name__ == '__main__':
    asyncio.run(main())

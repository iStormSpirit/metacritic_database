import sqlite3

con_sync = sqlite3.connect('../games_roulette.db')


def get_feed():
    cur = con_sync.cursor()
    cur.execute("""
               INSERT INTO publisher
                 (id, name)
               VALUES
                 (2, 'qwerty2')
            """, )
    con_sync.commit()
    con_sync.close()


def main():
    get_feed()

if __name__ == '__main__':
    main()
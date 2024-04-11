from functions import get_repos_stats
from postgres_db import PostgresDB
from config import config


def go():
    username = 'SergeyGladkovD'
    params = config()
    data = get_repos_stats(username)
    conn = PostgresDB(params)
    PostgresDB.create_table(conn)
    PostgresDB.add_data_in_table(conn, data)


if __name__ == "__main__":
    go()

import psycopg2


class PostgresDB:

    def __init__(self,  params) -> None:
        """ Инициализируем подключение к базе данных. """
        self.conn = psycopg2.connect(**params)

    def create_table(self):
        with self.conn.cursor()as cur:
            cur.execute("""
            CREATE TABLE test(
            x_id int,
            x_name VARCHAR(100),
            x_url VARCHAR(100))
            """)
        self.conn.commit()

    def add_data_in_table(self, data):
        with self.conn.cursor()as cur:
            for i in data:
                cur.execute(f"""
                INSERT INTO test (x_id, x_name, x_url) VALUES ('{i['id']}', '{i['name']}', '{i['full_name']}')""")
        self.conn.commit()
        self.conn.close()

import psycopg2
from django.conf import settings


class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )

    def execute_query(self, query, fetch=False):
        try:
            with self.conn as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    if fetch:
                        return cursor.fetchall()
                    conn.commit()
        except Exception as e:
            raise Exception(f"Query failed: {e}")

    def create_table(self, table_name):
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        self.execute_query(query)
        print(f"Table {table_name} created successfully.")

    def drop_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name};"
        self.execute_query(query)
        print(f"Table {table_name} dropped successfully.")

    def get_all_tables(self):
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        res = self.execute_query(query, fetch=True)
        for elem in res:
            print(elem)

    def insert(self, table_name, **kwargs):
        columns = ', '.join(kwargs.keys())
        values = ', '.join([f"'{v}'" for v in kwargs.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        self.execute_query(query)

    def select(self, table_name, *columns):
        columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table_name};"
        res = self.execute_query(query, fetch=True)
        print(type(res))
        for elem in res:
            print(elem)
        return res


def connect_to_db():
    return psycopg2.connect(
        dbname='formationdjango',
        user='postgres',
        password='secret',
        host='localhost',
        port='5432'
    )


def get_all_tables(cursor):
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    print(tables)


def create_table(table_name: str = 'ex00_movies'):
    """
    Create a table in the PostgreSQL database.
    """
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        cursor.execute(query)
        conn.commit()

        get_all_tables(cursor)
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        raise e

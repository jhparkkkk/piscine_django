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

    def disconnect(self):
        self.conn.close()

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

    def get_table_columns(self, table_name):
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{
            table_name}';"
        try:
            res = self.execute_query(query, fetch=True)
            print(res)
            columns = [row[0] for row in res]
            print(f"Columns for table {table_name}: {columns}")
            return columns
        except Exception as e:
            raise Exception(f"Failed to fetch columns for table {
                            table_name}: {e}")

    def alter_table(self, table_name, column_name, column_type, *constraints):
        constraints_str = ' '.join(constraints)
        query = f"ALTER TABLE {table_name} ADD COLUMN IF NOT EXISTS {
            column_name} {column_type} {constraints_str};"
        self.execute_query(query)
        print(f"Column {column_name} added to table {table_name}.")

    def drop_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name};"
        self.execute_query(query)
        print(f"Table {table_name} dropped successfully.")

    def get_all_tables(self):
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        res = self.execute_query(query, fetch=True)
        for elem in res:
            print(elem)

    def create_trigger_function(self, function_name):
        """Crée une fonction pour mettre à jour la colonne 'updated'."""
        query = f"""
        CREATE OR REPLACE FUNCTION {function_name}()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
        END;
        $$ LANGUAGE 'plpgsql';
        """
        self.execute_query(query)

    def create_trigger(self, table_name, trigger_name, function_name):
        query_check = f"""
        SELECT EXISTS (
            SELECT 1
            FROM pg_trigger
            WHERE tgname = '{trigger_name}'
        );
        """
        result = self.execute_query(query_check, fetch=True)
        if result and result[0][0]:
            print(f"Trigger '{trigger_name}' already exists for table '{
                  table_name}'.")
            return
        self.create_trigger_function(function_name)
        query = f"""
        CREATE TRIGGER {trigger_name}
        BEFORE UPDATE ON {table_name}
        FOR EACH ROW EXECUTE FUNCTION {function_name}();
        """
        self.execute_query(query)

    def select_if_exists(self, table_name, column, value):
        query = f"SELECT * FROM {table_name} WHERE {column} = '{value}';"
        res = self.execute_query(query, fetch=True)
        return res

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

    def delete(self, table_name, column, value):
        query = f"DELETE FROM {table_name} WHERE {column} = '{value}';"
        self.execute_query(query)
        print(f"Deleted {value} from {table_name}.")

    def update(self, table_name, column, value, data):
        data_str = ', '.join([f"{k} = '{v}'" for k, v in data.items()])
        query = f"UPDATE {table_name} SET {
            data_str} WHERE {column} = '{value}';"
        self.execute_query(query)
        print(f"Updated {value} in {table_name}.")

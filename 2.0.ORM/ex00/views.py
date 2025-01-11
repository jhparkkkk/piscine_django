from django.shortcuts import render
from django.http import HttpResponse

import psycopg2


def init(request):
    try:
        conn = psycopg2.connect(
            dbname='formationdjango',
            user='postgres',
            password='secret',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()
        print(tables)
        query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
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

        cursor.execute(
            "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'ex00_movies';")
        columns = cursor.fetchall()
        for col in columns:
            print(col)
        cursor.close()
        conn.close()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(f'Error creating ex00_movies: {e}')

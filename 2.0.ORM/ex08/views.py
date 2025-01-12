from django.shortcuts import render
from ex06.views import Ex06MoviesViews
from utils.SQLDatabaseManager import DatabaseManager
# Create your views here.
from pathlib import Path
from django.http import HttpResponse

path = Path(__file__).resolve().parent.parent


class Ex08Views(Ex06MoviesViews):
    def init(self, request):
        try:
            db_manager = DatabaseManager()
            query_planets = """
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INT,
                orbital_period INT,
                population BIGINT,
                rotation_period INT,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            """
            query_people = """
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass REAL,
                homeworld VARCHAR(64),
                CONSTRAINT fk_planet FOREIGN KEY (homeworld) REFERENCES ex08_planets (name)
            );
            """
            db_manager.execute_query(query_planets)
            db_manager.execute_query(query_people)
            return (HttpResponse("OK"))

        except Exception as e:
            return HttpResponse(f'Error initializing {self.table_name}: {e}')

    def populate(self, request):
        try:
            db_manager = DatabaseManager()
            planets_file = path / 'data' / 'planets.csv'
            people_file = path / 'data' / 'people.csv'

            with open(planets_file, 'r') as file:
                db_manager.conn.cursor().copy_expert(
                    f"""
                    COPY ex08_planets(name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                    FROM STDIN WITH CSV HEADER
                    """,
                    file
                )
            with open(people_file, 'r') as file:
                db_manager.conn.cursor().copy_expert(
                    f"""
                    COPY ex08_people(name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                    FROM STDIN WITH CSV HEADER
                    """,
                    file
                )

            db_manager.conn.commit()
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(f'Error populating {self.table_name}: {e}')

    def display(self, request):
        return super().display(request)

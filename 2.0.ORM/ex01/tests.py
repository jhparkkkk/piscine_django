from django.db.utils import IntegrityError, DataError
from django.test import TestCase
from .models import Movies
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db import transaction


class MoviesModelTest(TestCase):
    def setUp(self):
        # Crée un enregistrement de base pour les tests
        self.movie = Movies.objects.create(
            title='Interstellar',
            episode_nb=1,
            opening_crawl='A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
            director='Christopher Nolan',
            producer='Emma Thomas, Christopher Nolan',
            release_date='2014-11-07'
        )

    def test_movie_creation(self):
        movie = Movies.objects.get(title='Interstellar')
        self.assertEqual(movie.director, 'Christopher Nolan')
        self.assertEqual(movie.producer, 'Emma Thomas, Christopher Nolan')
        self.assertEqual(str(movie.release_date), '2014-11-07')
        self.assertEqual(movie.episode_nb, 1)
        self.assertEqual(
            movie.opening_crawl, 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.')

    def test_str_method(self):
        movie = Movies.objects.get(title='Interstellar')
        self.assertEqual(str(movie), 'Interstellar')

    def test_unique_title(self):
        with self.assertRaises(IntegrityError):
            Movies.objects.create(
                title='Interstellar',  # Doublon
                episode_nb=2,
                opening_crawl='',
                director='Another Director',
                producer='Another Producer',
                release_date='2020-01-01'
            )

    def test_unique_episode_nb(self):
        with self.assertRaises(IntegrityError):
            Movies.objects.create(
                title='Another Movie',
                episode_nb=1,
                opening_crawl='',
                director='Another Director',
                producer='Another Producer',
                release_date='2020-01-01'
            )

    def test_opening_crawl_null(self):
        movie = Movies.objects.create(
            title='Dunkirk',
            episode_nb=2,
            opening_crawl=None,
            director='Christopher Nolan',
            producer='Emma Thomas',
            release_date='2017-07-21'
        )
        self.assertIsNone(movie.opening_crawl)

    def test_field_length_constraints(self):
        with transaction.atomic():
            with self.assertRaises(DataError):
                Movies.objects.create(
                    title='Long Director Name Test',
                    episode_nb=3,
                    opening_crawl='',
                    director='x' * 33,
                    producer='Emma Thomas',
                    release_date='2022-12-01'
                )

        with transaction.atomic():
            with self.assertRaises(DataError):
                Movies.objects.create(
                    title='Long Producer Name Test',
                    episode_nb=4,
                    opening_crawl='',
                    director='Christopher Nolan',
                    producer='x' * 129,
                    release_date='2023-01-01'
                )

    def test_field_not_null_constraints(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Movies.objects.create(
                    title=None,
                    episode_nb=5,
                    opening_crawl='',
                    director='Christopher Nolan',
                    producer='Emma Thomas',
                    release_date='2024-01-01'
                )

    def test_date_field_format(self):
        with self.assertRaises(ValueError):
            Movies.objects.create(
                title='Invalid Date Test',
                episode_nb=7,
                opening_crawl='',
                director='Christopher Nolan',
                producer='Emma Thomas',
                release_date=datetime.strptime(
                    'Invalid Date', '%Y-%m-%d')
            )

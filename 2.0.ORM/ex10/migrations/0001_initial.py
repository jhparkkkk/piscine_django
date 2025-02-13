# Generated by Django 5.1.4 on 2025-01-31 10:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('birth_year', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('eye_color', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('hair_color', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('mass', models.FloatField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('climate', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('diameter', models.IntegerField(blank=True, default=0, null=True)),
                ('orbital_period', models.IntegerField(blank=True, default=0, null=True)),
                ('population', models.BigIntegerField(blank=True, default=0, null=True)),
                ('rotation_period', models.IntegerField(blank=True, default=0, null=True)),
                ('surface_water', models.FloatField(blank=True, default=0, null=True)),
                ('terrain', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('opening_crawl', models.TextField(blank=True, null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('characters', models.ManyToManyField(related_name='movies', to='ex10.people')),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ex10.planets'),
        ),
    ]

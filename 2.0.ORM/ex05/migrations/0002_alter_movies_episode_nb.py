# Generated by Django 5.1.4 on 2025-01-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex05', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='episode_nb',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

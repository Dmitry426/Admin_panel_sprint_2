# Generated by Django 3.2 on 2021-12-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_aded_unique_constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='genre',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(through='movies.PersonFilmWork', to='movies.Person'),
        ),
    ]

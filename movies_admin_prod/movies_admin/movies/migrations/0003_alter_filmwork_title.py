# Generated by Django 3.2 on 2021-12-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211207_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='title',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
    ]

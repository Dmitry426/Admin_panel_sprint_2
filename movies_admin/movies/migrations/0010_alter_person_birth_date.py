# Generated by Django 3.2 on 2021-12-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0009_alter_filmwork_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="birth_date"),
        ),
    ]

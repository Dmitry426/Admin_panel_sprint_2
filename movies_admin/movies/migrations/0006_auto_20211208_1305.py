# Generated by Django 3.2 on 2021-12-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_filmwork_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filmwork",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="person",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.0.2 on 2024-08-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_movie_actors_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='db.Genre'),
        ),
    ]

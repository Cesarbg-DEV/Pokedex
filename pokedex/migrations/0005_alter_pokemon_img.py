# Generated by Django 3.2.6 on 2021-11-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_pokemon_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_alter_pokemon_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadistica',
            name='pokemon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon'),
        ),
    ]

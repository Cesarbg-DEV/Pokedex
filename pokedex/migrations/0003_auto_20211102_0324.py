# Generated by Django 3.2.6 on 2021-11-02 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_pokemon_especie2'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadistica',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon'),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon'),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon'),
        ),
    ]
# Generated by Django 3.1.14 on 2022-05-13 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=None, verbose_name='Широта')),
                ('lon', models.FloatField(default=None, verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(default=None)),
                ('disappeared_at', models.DateTimeField(default=None)),
                ('level', models.IntegerField(default=None)),
                ('health', models.IntegerField(default=None)),
                ('strength', models.IntegerField(default=None)),
                ('defence', models.IntegerField(default=None)),
                ('stamina', models.IntegerField(default=None)),
                ('pokemon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]

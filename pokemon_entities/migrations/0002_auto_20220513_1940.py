# Generated by Django 3.1.14 on 2022-05-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]

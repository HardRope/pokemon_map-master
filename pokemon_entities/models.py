from django.db import models  # noqa F401

class Pokemon(models.Model):
    previous_evolution = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='evolution',
        verbose_name='Предыдущее поколение'
        )

    title = models.CharField('Имя', max_length=200)
    title_en = models.CharField('Имя на английском', blank=True, max_length=200)
    title_jp = models.CharField('Имя на японском', blank=True, max_length=200)

    image = models.ImageField('Изображение', default=None, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entity',
        verbose_name='Покемон'
    )

    lat = models.FloatField(default=None, verbose_name='Широта')
    lon = models.FloatField(default=None,   verbose_name='Долгота')


    appeared_at = models.DateTimeField('Время появления', default=None)
    disappeared_at = models.DateTimeField('Время исчезновения', default=None)

    level = models.IntegerField('Уровень', blank=True, null=True, default=None)
    health = models.IntegerField('Здоровье', blank=True, null=True, default=None)
    strength = models.IntegerField('Сила', blank=True, null=True, default=None)
    defence = models.IntegerField('Защита', blank=True, null=True, default=None)
    stamina = models.IntegerField('Выносливость', blank=True, null=True, default=None)

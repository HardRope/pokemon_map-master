from django.db import models  # noqa F401

class Pokemon(models.Model):
    previous_evolution = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='evolutions',
        verbose_name='Предыдущее поколение'
        )

    title = models.CharField('Имя', max_length=200)
    title_en = models.CharField('Имя на английском', blank=True, max_length=200)
    title_jp = models.CharField('Имя на японском', blank=True, max_length=200)

    image = models.ImageField('Изображение', default=None, blank=True, null=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name='Покемон'
    )

    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')


    appeared_at = models.DateTimeField('Время появления')
    disappeared_at = models.DateTimeField('Время исчезновения')

    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)

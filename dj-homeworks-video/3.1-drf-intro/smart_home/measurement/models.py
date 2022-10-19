from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')


class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        verbose_name='Сенсор',
    )
    temperature = models.FloatField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, verbose_name='Изображение')

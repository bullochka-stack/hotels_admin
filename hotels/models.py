from django.core.validators import validate_email
from django.db import models
from phonenumber_field.validators import validate_international_phonenumber


class City(models.Model):
    name = models.CharField('Название города', max_length=170)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Hotel(models.Model):
    name = models.CharField('Название отеля', max_length=200)
    email = models.EmailField('Email', validators=[validate_email])
    phone = models.CharField(
        'Номер телефона',
        max_length=20,
        validators=[validate_international_phonenumber]
    )
    city = models.ForeignKey(
        City,
        verbose_name='Город',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Отель: {self.name} - {self.city}'

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

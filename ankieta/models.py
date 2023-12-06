from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Ankieta(models.Model):
    wiek = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    wzrost = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        validators=[
            MaxValueValidator(2.5),
            MinValueValidator(1.2)
        ]
    )
    płeć = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Mężczyzna'),
            ('K', 'Kobieta')
        ]
    )
    ulubiony_kolor = models.CharField(max_length=64)







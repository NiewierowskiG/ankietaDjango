from django.db import models


class Ankieta(models.Model):
    wiek = models.PositiveSmallIntegerField()
    wzrost = models.DecimalField(decimal_places=2, max_digits=3)
    płeć = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Mężczyzna'),
            ('K', 'Kobieta')
        ]
    )
    ulubiony_kolor = models.CharField(max_length=64)







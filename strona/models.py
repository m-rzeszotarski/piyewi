from django.db import models
from django.utils import timezone

class Yerba(models.Model):

    NUMERY = [
        (0, '0'),
        (0.5, '0.5'),
        (1, '1'),
        (1.5, '1.5'),
        (2, '2'),
        (2.5, '2.5'),
        (3, '3'),
        (3.5, '3.5'),
        (4, '4'),
        (4.5, '4.5'),
        (5, '5'),
        (5.5, '5.5'),
        (6, '6'),
        (6.5, '6.5'),
        (7, '7'),
        (7.5, '7.5'),
        (8, '8'),
        (8.5, '8.5'),
        (9, '9'),
        (9.5, '9.5'),
        (10, '10'),
    ]

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    zapylenie = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    aromat = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    moc = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    goryczka = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    nuty_owocowe = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    ocena = models.PositiveSmallIntegerField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa


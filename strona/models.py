from django.db import models
from django.utils import timezone

## yerba

class Yerba(models.Model):

    NUMERY = [
        (0.0, '0'),
        (0.5, '0.5'),
        (1.0, '1'),
        (1.5, '1.5'),
        (2.0, '2'),
        (2.5, '2.5'),
        (3.0, '3'),
        (3.5, '3.5'),
        (4.0, '4'),
        (4.5, '4.5'),
        (5.0, '5'),
        (5.5, '5.5'),
        (6.0, '6'),
        (6.5, '6.5'),
        (7.0, '7'),
        (7.5, '7.5'),
        (8.0, '8'),
        (8.5, '8.5'),
        (9.0, '9'),
        (9.5, '9.5'),
        (10.0, '10'),
    ]

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    zapylenie = models.FloatField(
        choices=NUMERY,
        default=0
    )
    aromat = models.FloatField(
        choices=NUMERY,
        default=0
    )
    moc = models.FloatField(
        choices=NUMERY,
        default=0
    )
    goryczka = models.FloatField(
        choices=NUMERY,
        default=0
    )
    nuty_owocowe = models.FloatField(
        choices=NUMERY,
        default=0
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

## piwo

class Piwo(models.Model):

    NUMERY = [
        (0.0, '0'),
        (0.5, '0.5'),
        (1.0, '1'),
        (1.5, '1.5'),
        (2.0, '2'),
        (2.5, '2.5'),
        (3.0, '3'),
        (3.5, '3.5'),
        (4.0, '4'),
        (4.5, '4.5'),
        (5.0, '5'),
        (5.5, '5.5'),
        (6.0, '6'),
        (6.5, '6.5'),
        (7.0, '7'),
        (7.5, '7.5'),
        (8.0, '8'),
        (8.5, '8.5'),
        (9.0, '9'),
        (9.5, '9.5'),
        (10.0, '10'),
    ]

    JASNE = 'jasne'
    CIEMNE = 'ciemne'
    TYP_PIWA = [
        (JASNE, 'jasne'),
        (CIEMNE, 'ciemne'),
    ]

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)

    typ = models.CharField(
        max_length=32,
        choices=TYP_PIWA,
        default=JASNE,
    )
    aromat = models.FloatField(
        choices=NUMERY,
        default=0
    )
    smak = models.FloatField(
        choices=NUMERY,
        default=0
    )
    moc = models.FloatField(
        choices=NUMERY,
        default=0
    )
    goryczka = models.FloatField(
        choices=NUMERY,
        default=0
    )
    nuty_owocowe = models.FloatField(
        choices=NUMERY,
        default=0
    )
    piana = models.FloatField(
        choices=NUMERY,
        default=0
    )
    kolor = models.FloatField(
        choices=NUMERY,
        default=0
    )
    mętność = models.FloatField(
        choices=NUMERY,
        default=0
    )
    zgazowanie = models.FloatField(
        choices=NUMERY,
        default=0
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

## Wino

class Wino(models.Model):

    NUMERY = [
        (0.0, '0'),
        (0.5, '0.5'),
        (1.0, '1'),
        (1.5, '1.5'),
        (2.0, '2'),
        (2.5, '2.5'),
        (3.0, '3'),
        (3.5, '3.5'),
        (4.0, '4'),
        (4.5, '4.5'),
        (5.0, '5'),
        (5.5, '5.5'),
        (6.0, '6'),
        (6.5, '6.5'),
        (7.0, '7'),
        (7.5, '7.5'),
        (8.0, '8'),
        (8.5, '8.5'),
        (9.0, '9'),
        (9.5, '9.5'),
        (10.0, '10'),
    ]

    BIAŁE = 'białe'
    CZERWONE = 'czerwone'
    RÓŻOWE = 'różowe'
    TYP_WINA = [
        (BIAŁE, 'białe'),
        (CZERWONE, 'czerwone'),
        (RÓŻOWE, 'różowe'),
    ]

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    typ = models.CharField(
        max_length=32,
        choices=TYP_WINA,
        default=BIAŁE,
    )
    kolor = models.FloatField(
        choices=NUMERY,
        default=0
    )
    klarowność = models.FloatField(
        choices=NUMERY,
        default=0
    )
    musowanie = models.FloatField(
        choices=NUMERY,
        default=0
    )
    aromat = models.FloatField(
        choices=NUMERY,
        default=0
    )
    moc = models.FloatField(
        choices=NUMERY,
        default=0
    )
    nuty_owocowe = models.FloatField(
        choices=NUMERY,
        default=0
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

## kawa

class Kawa(models.Model):

    NUMERY = [
        (0.0, '0'),
        (0.5, '0.5'),
        (1.0, '1'),
        (1.5, '1.5'),
        (2.0, '2'),
        (2.5, '2.5'),
        (3.0, '3'),
        (3.5, '3.5'),
        (4.0, '4'),
        (4.5, '4.5'),
        (5.0, '5'),
        (5.5, '5.5'),
        (6.0, '6'),
        (6.5, '6.5'),
        (7.0, '7'),
        (7.5, '7.5'),
        (8.0, '8'),
        (8.5, '8.5'),
        (9.0, '9'),
        (9.5, '9.5'),
        (10.0, '10'),
    ]

    SKŁAD = [(i,i) for i in range(101)]

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    arabica = models.PositiveSmallIntegerField(
        choices = SKŁAD,
        default= 0
    )
    robusta = models.PositiveSmallIntegerField(
        choices = SKŁAD,
        default= 0
    )
    stopień_palenia = models.FloatField(
        choices=NUMERY,
        default=0
    )
    kwasowość = models.FloatField(
        choices=NUMERY,
        default=0
    )
    moc = models.FloatField(
        choices=NUMERY,
        default=0
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa
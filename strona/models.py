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

    autor = models.CharField(max_length=200)
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
    trwałość = models.FloatField(
        choices=NUMERY,
        default=0
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)
    zatwierdzony = models.BooleanField(default=False)

    def zatwierdzenie(self):
        self.zatwierdzony = True
        self.save()

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

    autor = models.CharField(max_length=200)
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

    zatwierdzony = models.BooleanField(default=False)

    def zatwierdzenie(self):
        self.zatwierdzony = True
        self.save()

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

    TAK = 'tak'
    NIE = 'nie'
    TAKNIE = [
        (TAK, 'tak'),
        (NIE, 'nie'),
    ]

    WYTRAWNE = 'wytrawne'
    PÓŁWYTRAWNE = 'półwytrawne'
    PÓŁSŁODKIE = 'półsłodkie'
    SŁODKIE = 'słodkie'
    ZAW_CUK = [
        (WYTRAWNE, 'wytrawne'),
        (PÓŁWYTRAWNE, 'półwytrawne'),
        (PÓŁSŁODKIE, 'półsłodkie'),
        (SŁODKIE, 'słodkie'),
    ]

    autor = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    typ = models.CharField(
        max_length=32,
        choices=TYP_WINA,
        default=BIAŁE,
    )
    zawartość_cukru = models.CharField(
        max_length=32,
        choices=ZAW_CUK,
        default=WYTRAWNE,
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
    nuty_zielonych_owoców = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_czerwonych_owoców = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_czarnych_owoców = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_cytrusowe = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_tropikalne = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_pestkowców = models.CharField(
        max_length=32,
        choices=TAKNIE,
        default=NIE
    )
    nuty_suszonych_owoców = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_roślinne = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_kwiatowe = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_drożdżowe = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_dojrzewające = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_maślane = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_dębowe = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_ziemne = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    nuty_minerałów = models.CharField(
        max_length=32,
        choices = TAKNIE,
        default=NIE
    )
    ocena = models.FloatField(
        choices=NUMERY,
        default=0
    )
    uwagi = models.TextField(blank=True, null=True)

    zatwierdzony = models.BooleanField(default=False)

    def zatwierdzenie(self):
        self.zatwierdzony = True
        self.save()

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

    autor = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    firma = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    arabica = models.PositiveSmallIntegerField(
        choices = SKŁAD,
        default= 0
    )
    
    def robusta(self):
        return 100 - int(self.arabica)

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

    zatwierdzony = models.BooleanField(default=False)

    def zatwierdzenie(self):
        self.zatwierdzony = True
        self.save()

    def __str__(self):
        return self.nazwa
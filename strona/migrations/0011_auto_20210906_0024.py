# Generated by Django 3.2.6 on 2021-09-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0010_auto_20210905_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='kawa',
            name='zatwierdzony',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='piwo',
            name='zatwierdzony',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wino',
            name='zatwierdzony',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='yerba',
            name='zatwierdzony',
            field=models.BooleanField(default=False),
        ),
    ]

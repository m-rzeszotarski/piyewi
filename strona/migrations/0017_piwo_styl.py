# Generated by Django 3.2.6 on 2021-10-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0016_wino_zawartość_cukru'),
    ]

    operations = [
        migrations.AddField(
            model_name='piwo',
            name='styl',
            field=models.CharField(default='styl', max_length=200),
        ),
    ]

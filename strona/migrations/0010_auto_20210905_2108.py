# Generated by Django 3.2.6 on 2021-09-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0009_remove_kawa_robusta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kawa',
            name='autor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='autor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wino',
            name='autor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='yerba',
            name='autor',
            field=models.CharField(max_length=200),
        ),
    ]
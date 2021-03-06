# Generated by Django 3.2.6 on 2021-09-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0004_piwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piwo',
            name='aromat',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='goryczka',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='kolor',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='moc',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='mętność',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='nuty_owocowe',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='ocena',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='piana',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='smak',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='piwo',
            name='zgazowanie',
            field=models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5'), (5.5, '5.5'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10')], default=0),
        ),
    ]

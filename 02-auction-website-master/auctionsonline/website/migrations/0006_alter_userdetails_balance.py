# Generated by Django 4.0.6 on 2022-07-31 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220730_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=16),
        ),
    ]

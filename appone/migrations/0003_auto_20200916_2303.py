# Generated by Django 2.2 on 2020-09-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_auto_20200916_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

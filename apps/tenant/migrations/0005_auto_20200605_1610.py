# Generated by Django 2.0.2 on 2020-06-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0004_auto_20200605_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Location'),
        ),
    ]

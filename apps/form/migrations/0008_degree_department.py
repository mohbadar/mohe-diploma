# Generated by Django 3.0.7 on 2020-06-28 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20200628_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='department',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, help_text='Department', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
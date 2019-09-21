# Generated by Django 2.2.5 on 2019-09-05 07:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, max_length=250),
            preserve_default=False,
        ),
    ]
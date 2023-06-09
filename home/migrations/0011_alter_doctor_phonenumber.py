# Generated by Django 4.1.3 on 2022-11-23 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phonenumber',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]

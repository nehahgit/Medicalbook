# Generated by Django 3.0.4 on 2020-06-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phonenumber',
            field=models.CharField(max_length=10),
        ),
    ]

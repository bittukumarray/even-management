# Generated by Django 2.2.4 on 2019-11-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='check_in',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='check_out',
            field=models.TimeField(auto_now_add=True),
        ),
    ]

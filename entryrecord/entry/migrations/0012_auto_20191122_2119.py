# Generated by Django 2.2.4 on 2019-11-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0011_auto_20191122_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='check_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

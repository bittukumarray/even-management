# Generated by Django 2.2.4 on 2019-11-22 19:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0006_auto_20191122_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=10, unique=True),
        ),
    ]

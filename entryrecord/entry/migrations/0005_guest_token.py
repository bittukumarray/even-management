# Generated by Django 2.2.4 on 2019-11-22 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_auto_20191122_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
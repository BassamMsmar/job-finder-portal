# Generated by Django 4.2.2 on 2023-10-14 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 11, 52, 1, 537769, tzinfo=datetime.timezone.utc)),
        ),
    ]

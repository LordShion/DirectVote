# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 168000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 168000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='votation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 170000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='votation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 171000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='votation',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 170000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='votation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 8, 21, 58, 170000, tzinfo=utc), editable=False),
        ),
    ]

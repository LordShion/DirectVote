# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160813_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='created_by',
            field=models.ForeignKey(related_name='Proposal_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='modified_by',
            field=models.ForeignKey(related_name='Proposal_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='votation',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votation',
            name='created_by',
            field=models.ForeignKey(related_name='Votation_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='votation',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votation',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votation',
            name='modified_by',
            field=models.ForeignKey(related_name='Votation_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='votation',
            name='nb_blank_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votation',
            name='nb_con_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votation',
            name='nb_pro_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votation',
            name='proposal',
            field=models.OneToOneField(to='main.Proposal'),
        ),
        migrations.AlterField(
            model_name='votation',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votation',
            name='total_available_voters',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votation',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]

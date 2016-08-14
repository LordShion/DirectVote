# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Proposal Title', max_length=512)),
                ('text', models.TextField(default=b'Proposal text', max_length=20000)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValidUser',
            fields=[
                ('idcard', models.BigIntegerField(serialize=False, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Votation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Proposal Title', max_length=512)),
                ('nb_pro_votes', models.IntegerField(default=0, editable=False)),
                ('nb_con_votes', models.IntegerField(default=0, editable=False)),
                ('nb_blank_votes', models.IntegerField(default=0, editable=False)),
                ('total_votes', models.IntegerField(default=0, editable=False)),
                ('total_available_voters', models.IntegerField(default=0, editable=False)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('start_date', models.DateTimeField(editable=False)),
                ('end_date', models.DateTimeField(editable=False)),
                ('created_by', models.ForeignKey(related_name='Votation_created_by', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='Votation_modified_by', editable=False, to=settings.AUTH_USER_MODEL)),
                ('proposal', models.OneToOneField(editable=False, to='main.Proposal')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='authors',
            field=models.ManyToManyField(to='main.ValidUser'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='created_by',
            field=models.ForeignKey(related_name='Proposal_created_by', editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proposal',
            name='modified_by',
            field=models.ForeignKey(related_name='Proposal_modified_by', editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='validuser',
            unique_together=set([('user', 'idcard')]),
        ),
    ]

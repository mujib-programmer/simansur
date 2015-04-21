# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpencatatsurat',
            name='bidang',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AlterField(
            model_name='userpencatatsurat',
            name='jabatan',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AlterField(
            model_name='userpenerimasurat',
            name='bidang',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AlterField(
            model_name='userpenerimasurat',
            name='jabatan',
            field=models.CharField(max_length=40, default=''),
        ),
    ]

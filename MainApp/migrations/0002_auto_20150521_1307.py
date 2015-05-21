# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='keterangan_disposisi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tracksurat',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]

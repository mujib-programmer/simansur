# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20150507_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='no_telepon',
            field=models.CharField(max_length=15, default=''),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20150421_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='timestamp_disposisi',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='surat',
            name='timestamp_surat',
            field=models.DateTimeField(),
        ),
    ]

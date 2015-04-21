# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20150421_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='tanggal_surat_disposisi',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='disposisi',
            name='timestamp_disposisi',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='timestamp_surat',
            field=models.TimeField(auto_now=True),
        ),
    ]

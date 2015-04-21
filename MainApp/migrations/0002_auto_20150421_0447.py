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
            name='tanggal_surat_disposisi',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='surat',
            name='timestamp_surat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

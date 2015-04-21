# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20150421_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='timestamp_disposisi',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='tanggal_surat_masuk',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='surat',
            name='timestamp_surat',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

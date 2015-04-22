# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20150422_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='dari',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='keterangan_disposisi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='perihal_surat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='tanggal_surat_masuk',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='timestamp_surat',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='tingkat_kepentingan',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

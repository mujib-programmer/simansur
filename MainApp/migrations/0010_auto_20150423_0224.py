# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_auto_20150422_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='id_penerima_disposisi',
            field=models.ForeignKey(to='MainApp.UserProfile', related_name='id_penerima_disposisi'),
        ),
        migrations.AlterField(
            model_name='disposisi',
            name='id_pengirim_disposisi',
            field=models.ForeignKey(to='MainApp.UserProfile', related_name='id_pengirim_disposisi'),
        ),
        migrations.AlterField(
            model_name='surat',
            name='file_surat',
            field=models.FileField(null=True, upload_to='/home/phpgeek/PycharmProjects/simansur/static/upload', blank=True),
        ),
        migrations.AlterField(
            model_name='surat',
            name='id_pencatat',
            field=models.ForeignKey(to='MainApp.UserProfile', null=True, related_name='id_pencatat'),
        ),
        migrations.AlterField(
            model_name='surat',
            name='id_penerima',
            field=models.ForeignKey(to='MainApp.UserProfile', null=True, related_name='id_penerima'),
        ),
    ]

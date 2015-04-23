# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20150423_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disposisi',
            old_name='no_surat_disposisi',
            new_name='surat',
        ),
        migrations.RemoveField(
            model_name='disposisi',
            name='id_penerima_disposisi',
        ),
        migrations.RemoveField(
            model_name='disposisi',
            name='id_pengirim_disposisi',
        ),
        migrations.AddField(
            model_name='disposisi',
            name='penerima_disposisi',
            field=models.ForeignKey(related_name='penerima_disposisi', null=True, to='MainApp.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disposisi',
            name='pengirim_disposisi',
            field=models.ForeignKey(related_name='pengirim_disposisi', null=True, to='MainApp.UserProfile'),
            preserve_default=True,
        ),
    ]

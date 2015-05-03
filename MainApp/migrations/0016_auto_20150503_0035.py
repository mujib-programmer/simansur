# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_auto_20150502_0511'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackSurat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(null=True, auto_now_add=True)),
                ('surat', models.ForeignKey(to='MainApp.Surat', related_name='surat_di_track_surat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='surat',
            name='no_agenda',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='surat',
            name='no_surat',
            field=models.CharField(unique=True, max_length=15),
        ),
    ]

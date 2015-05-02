# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_auto_20150423_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='aktivitas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(null=True, auto_now_add=True)),
                ('aktivitas', models.CharField(max_length=255)),
                ('user_profile', models.ForeignKey(null=True, to='MainApp.UserProfile', related_name='user_profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='surat',
            name='status_surat',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='surat',
            name='file_surat',
            field=models.FileField(blank=True, null=True, upload_to='/home/mujibur/PycharmProjects/simansur/static/upload'),
        ),
    ]

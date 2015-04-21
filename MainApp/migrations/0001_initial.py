# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disposisi',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('catatan_tambahan', models.CharField(max_length=25)),
                ('timestamp_disposisi', models.DateTimeField(auto_now=True)),
                ('tanggal_surat_disposisi', models.DateField()),
                ('id_penerima_disposisi', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='id_penerima_disposisi')),
                ('id_pengirim_disposisi', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='id_pengirim_disposisi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('no_surat', models.IntegerField(unique=True)),
                ('no_agenda', models.IntegerField()),
                ('perihal_surat', models.TextField()),
                ('tanggal_surat_masuk', models.DateTimeField()),
                ('keterangan_disposisi', models.TextField()),
                ('tingkat_kepentingan', models.CharField(max_length=15)),
                ('dari', models.TextField()),
                ('timestamp_surat', models.TimeField(auto_now=True)),
                ('id_pencatat', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='id_pencatat')),
                ('id_penerima', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='id_penerima')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('bidang', models.CharField(max_length=40, default='')),
                ('jabatan', models.CharField(max_length=40, default='')),
                ('role_pencatat', models.BooleanField(default=False)),
                ('no_telepon', models.BigIntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='disposisi',
            name='no_surat_disposisi',
            field=models.ForeignKey(to='MainApp.Surat', related_name='no_surat_disposisi'),
            preserve_default=True,
        ),
    ]

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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catatan_tambahan', models.CharField(max_length=25)),
                ('timestamp_disposisi', models.DateTimeField(auto_now=True)),
                ('tanggal_surat_disposisi', models.DateField()),
                ('id_penerima_disposisi', models.ForeignKey(related_name='id_penerima_disposisi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_surat', models.IntegerField(unique=True)),
                ('no_agenda', models.IntegerField()),
                ('perihal_surat', models.TextField()),
                ('tanggal_surat_masuk', models.DateTimeField()),
                ('keterangan_disposisi', models.TextField()),
                ('tingkat_kepentingan', models.CharField(max_length=15)),
                ('dari', models.TextField()),
                ('timestamp_surat', models.TimeField(auto_now=True)),
                ('id_pencatat', models.ForeignKey(related_name='id_pencatat', to=settings.AUTH_USER_MODEL)),
                ('id_penerima', models.ForeignKey(related_name='id_penerima', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPencatatSurat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bidang', models.CharField(default=b'', max_length=40)),
                ('jabatan', models.CharField(default=b'', max_length=40)),
                ('role_pencatat', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPenerimaSurat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bidang', models.CharField(default=b'', max_length=40)),
                ('jabatan', models.CharField(default=b'', max_length=40)),
                ('no_telepon', models.BigIntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='disposisi',
            name='no_surat_disposisi',
            field=models.ForeignKey(related_name='no_surat_disposisi', to='MainApp.Surat'),
        ),
        migrations.AddField(
            model_name='disposisi',
            name='user_name_pengirim_disposisi',
            field=models.ForeignKey(related_name='user_name_pengirim_disposisi', to=settings.AUTH_USER_MODEL),
        ),
    ]

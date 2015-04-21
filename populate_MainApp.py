# Script for populate dummy data to MainApp

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simansur.settings')

import django
django.setup()

from MainApp.models import Surat, Disposisi, UserProfile
from django.contrib.auth.models import User, Group
from datetime import datetime


def populate():
    #populate user, group, and userProfile
    admin_group = add_group("admin")
    pencatat_group = add_group("pencatat surat")
    penerima_group = add_group("penerima surat")

    pencatat_1_user = add_user("pencatat_1", "pencatat", "satu", "pencatat_1@localhost.com", "pencatat_1", pencatat_group)
    pencatat_2_user = add_user("pencatat_2", "pencatat", "dua", "pencatat_2@localhost.com", "pencatat_2", pencatat_group)

    penerima_1_user = add_user("penerima_1", "penerima", "satu", "penerima_1@localhost.com", "penerima_1", penerima_group)
    penerima_2_user = add_user("penerima_2", "penerima", "dua", "penerima_2@localhost.com", "penerima_2", penerima_group)


    pencatat_1_user_profile = add_user_profile(pencatat_1_user, "kepegawaian", "staf", False, "021234567")
    pencatat_2_user_profile = add_user_profile(pencatat_2_user, "kepegawaian", "staf", True, "021765432")
    penerima_1_user_profile = add_user_profile(penerima_1_user, "kepegawaian", "staf", False, "0210000001")
    penerima_2_user_profile = add_user_profile(penerima_2_user, "kepegawaian", "staf", False, "02100000002")

    # populate surat dan disposisi
    surat_1 = add_surat(1, 1, "perihal informasi", datetime.now(), "", "normal", "mahasiswa", datetime.now(), penerima_1_user_profile.user, pencatat_1_user_profile.user)
    surat_2 = add_surat(2, 2, "perihal gaji pegawai", datetime.now(), "", "penting", "dept keuangan", datetime.now(), penerima_2_user_profile.user, pencatat_2_user_profile.user)

    disposisi_surat_1 = add_disposisi(penerima_2_user_profile.user, surat_1, penerima_1_user_profile.user, "disposisi ke penerima 2", datetime.now(), datetime.now() )
    disposisi_2_surat_1 = add_disposisi(pencatat_2_user_profile.user, surat_1, penerima_2_user_profile.user, "disposisi ke pencatat 2", datetime.now(), datetime.now() )



    # Print out what we have added to the user.
    """
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))
    """

def add_group(name):
    # group has 2 fields (name, permissions)
    g = Group.objects.get_or_create(name=name)[0]

    return g

def add_user(username, first_name, last_name, email, password, groups):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    u.first_name = first_name
    u.last_name = last_name
    u.save()

    # set user groups
    groups.user_set.add(u)

    return u

def add_user_profile(user, bidang, jabatan, role_pencatat, no_telepon):
    up = UserProfile.objects.get_or_create(user=user, bidang=bidang, jabatan=jabatan, role_pencatat=role_pencatat, no_telepon=no_telepon)[0]

    return up

def add_surat(no_surat, no_agenda, perihal_surat, tanggal_surat_masuk, keterangan_disposisi, tingkat_kepentingan, dari, timestamp_surat, id_penerima, id_pencatat):
    s = Surat.objects.get_or_create(
        no_surat=no_surat, no_agenda=no_agenda, perihal_surat=perihal_surat, tanggal_surat_masuk=tanggal_surat_masuk,
        keterangan_disposisi=keterangan_disposisi, tingkat_kepentingan=tingkat_kepentingan, dari=dari,
        timestamp_surat=timestamp_surat, id_penerima=id_penerima, id_pencatat=id_pencatat)[0]

    return s

def add_disposisi(id_penerima_disposisi, no_surat_disposisi, id_pengirim_disposisi, catatan_tambahan, timestamp_disposisi, tanggal_surat_disposisi):
    d = Disposisi.objects.get_or_create(
        id_penerima_disposisi=id_penerima_disposisi, no_surat_disposisi=no_surat_disposisi,
        id_pengirim_disposisi=id_pengirim_disposisi, catatan_tambahan=catatan_tambahan,
        timestamp_disposisi=timestamp_disposisi, tanggal_surat_disposisi=tanggal_surat_disposisi)[0]

    return d

# Start execution here!
if __name__ == '__main__':
    print("Starting simansur MainApp population script...")
    populate()
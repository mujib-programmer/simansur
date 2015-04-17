from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Surat(models.Model):
    no_surat = models.IntegerField(unique=True)
    no_agenda = models.IntegerField()
    perihal_surat = models.TextField()
    tanggal_surat_masuk = models.DateTimeField(auto_now=False)
    keterangan_disposisi = models.TextField()
    tingkat_kepentingan = models.CharField(max_length=15)
    dari = models.TextField()
    timestamp_surat = models.TimeField(auto_now=True)
    id_penerima = models.ForeignKey(User, null=False, related_name='id_penerima')
    id_pencatat = models.ForeignKey(User, null=False, related_name='id_pencatat')
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return str( self.no_surat )

class Disposisi(models.Model):
    id_penerima_disposisi = models.ForeignKey(User, null=False, related_name='id_penerima_disposisi')
    no_surat_disposisi = models.ForeignKey(Surat, null=False, related_name='no_surat_disposisi')
    user_name_pengirim_disposisi = models.ForeignKey(User, null=False, related_name='user_name_pengirim_disposisi')
    catatan_tambahan = models.CharField(max_length=25)
    timestamp_disposisi = models.DateTimeField(auto_now=True)
    tanggal_surat_disposisi = models.DateField()
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return str( self.no_surat_disposisi )
    
    
# memperluas data dari model User khusus pencatat surat
class UserPencatatSurat(models.Model):   
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    bidang = models.CharField(max_length=40, default="")
    jabatan = models.CharField(max_length=40, default="")
    role_pencatat = models.BooleanField(default=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
# memperluas data dari model User khusus penerima surat
class UserPenerimaSurat(models.Model):   
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    bidang = models.CharField(max_length=40, default="")
    jabatan = models.CharField(max_length=40, default="")
    no_telepon = models.BigIntegerField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    

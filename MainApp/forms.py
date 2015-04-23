from django import forms
from django.contrib.auth.models import User
from MainApp.models import Surat, Disposisi, UserProfile

class SuratForm(forms.ModelForm):
    no_surat = forms.IntegerField(label='No Surat')
    no_agenda = forms.IntegerField(label='No Agenda')
    perihal_surat = forms.CharField(label='Perihal Surat')
    tanggal_surat_masuk = forms.DateField(label='Tanggal Surat Masuk')
    keterangan_disposisi = forms.CharField(label='Keterangan Disposisi')
    tingkat_kepentingan = forms.CharField(label='Tingkat Kepentingan')
    dari = forms.CharField(label='Dari')
    #timestamp_surat = forms.DateTimeField()
    id_penerima = forms.ModelChoiceField(label='Penerima', queryset=UserProfile.objects.all())
    id_pencatat = forms.ModelChoiceField(label='Pencatat', queryset=UserProfile.objects.all())
    file_surat = forms.FileField(label='File Surat')


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Surat
        fields = ('no_surat', 'no_agenda','perihal_surat', 'tanggal_surat_masuk', 'keterangan_disposisi', 'tingkat_kepentingan', 'dari', 'id_penerima', 'id_pencatat', 'file_surat',)


class DisposisiForm(forms.ModelForm):
    penerima_disposisi = forms.ModelChoiceField(label='Penerima Disposisi', queryset=UserProfile.objects.all())
    pengirim_disposisi = forms.ModelChoiceField(label='Pengirim Disposisi', queryset=UserProfile.objects.all())
    tanggal_surat_disposisi = forms.DateField(label='Tanggal Surat Disposisi')
    catatan_tambahan = forms.CharField(label='Catatan Tambahan')


    class Meta:
        model = Disposisi

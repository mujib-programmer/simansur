from django import forms
from django.contrib.auth.models import User, Group
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
        exclude = ('surat',)

class UserProfileForm(forms.Form):
    username = forms.SlugField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    groups = forms.ModelMultipleChoiceField(label="Groups", queryset=Group.objects.all())
    first_name = forms.CharField(label="Nama Depan", max_length=30)
    last_name = forms.CharField(label="Nama Belakang", max_length=30)
    is_active = forms.BooleanField(label="Status Aktif", required=False)
    jabatan = forms.CharField(label="Jabatan", max_length=40)
    bidang = forms.CharField(label="Bidang", max_length=40)
    no_telepon = forms.IntegerField(label="No Telepon")




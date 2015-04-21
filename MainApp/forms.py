from django import forms
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
    id_penerima = forms.ChoiceField(label='Penerima',
        choices=[(x.user,x.user) for x in UserProfile.objects.all()]
         )
    id_pencatat = forms.ChoiceField( label='Pencatat',
        choices=[(x.user,x.user) for x in UserProfile.objects.all()]
         )


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Surat
        fields = ('no_surat',)



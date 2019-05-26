from django import forms
from .models import Download

class DownloadForm(forms.ModelForm):
    url = forms.CharField()

    class Meta:
        model = Download
        fields = ('url',)
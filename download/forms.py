from django import forms
from .models import Download

class DownloadForm(forms.ModelForm):
    url = forms.URLField()

    class Meta:
        model = Download
        fields = ('url',)
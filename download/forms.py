from django import forms
from .models import Download
import re


class DownloadForm(forms.ModelForm):
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if re.match('^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+', url):
            return url
        else:
            raise forms.ValidationError("Bad URL! Enter YouTube url!")

    class Meta:
        model = Download
        fields = ('url',)

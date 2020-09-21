from django.forms import ModelForm, URLField, HiddenInput, TextInput, URLInput
from .models import Urlhacked


class UrlForm1(ModelForm):
    class Meta:
        model = Urlhacked
        fields = ['original_url', 'short_url']
        widgets = {'short_url': HiddenInput(), 'original_url': URLInput(
            attrs={'placeholder': 'Paste URL you would like to shorten', 'autofocus': 'autofocus'})}


class UrlForm2(ModelForm):
    class Meta:
        model = Urlhacked
        fields = ['original_url', 'short_url']
        widgets = {'short_url': TextInput(attrs={'readonly': 'readonly'}),
                   'original_url': TextInput(attrs={'readonly': 'readonly'})}

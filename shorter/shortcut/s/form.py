from django import forms


class ShortUrlForm(forms.Form):
    url = forms.URLField(label='url')

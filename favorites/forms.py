from django import forms

class NewFavoriteForm(forms.Form):
    name = forms.CharField()


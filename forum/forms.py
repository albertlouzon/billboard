from django import forms
from .models import Headlines

class Feed(forms.ModelForm):
    class Meta:
        model = Headlines
        fields = ('title')
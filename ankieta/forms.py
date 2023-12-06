from django import forms
from .models import Ankieta


class AnkietaForm(forms.ModelForm):
    class Meta:
        model = Ankieta
        fields = "__all__"

from . models import SoFDocument
from django import forms

class SoFDocumentForm(forms.ModelForm):
    class Meta:
        model = SoFDocument
        fields = ['file']
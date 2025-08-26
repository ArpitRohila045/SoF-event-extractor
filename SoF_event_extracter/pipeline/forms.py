from . models import SoFDocument
from django import forms
import os

class SoFDocumentForm(forms.ModelForm):
    class Meta:
        model = SoFDocument
        fields = ['file']
        widgets = {
            'file' : forms.FileInput(attrs={
                'class' : 'form-control-file',
                'accept' : '.pdf,.doc,.docx',
                'id' : 'file-uplaod',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].help_text = "Select a Pdf, Image or Word Document"

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Check file type

            allowed_extension = ['.pdf','doc','jpeg']
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in allowed_extension:
                raise forms.ValidationError("Unsupported Format")


        """
        Further the Format will be converted to the image
        """
        return file
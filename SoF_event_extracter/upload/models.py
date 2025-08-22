from django.db import models
from django.conf import settings


# Create your models here.
class SoFDocument(models.Model):
    FILE_TYPE = [
        ('pdf', 'PDF'),
        ('word', 'Word'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sof_documents")
    file = models.FileField(upload_to='sof_documnents/')
    file_type = models.CharField(max_length=11, choices=FILE_TYPE)
    uplaoded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.file_type})"
    
    
class SOFData(models.Model):
    documnent = models.ForeignKey(SoFDocument, on_delete=models.CASCADE, related_name='sof_date')
    extracted_data = models.JSONField()
    extracted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data from {self.documnent.file.name} by {self.documnent.user.username}"
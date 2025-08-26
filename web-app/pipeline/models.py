from django.db import models
from django.conf import settings
import uuid
import os

# Create your models here.

def user_directory_path(instance, filename):
    """File will be uploaded to MEDIA_ROOT/sof_documents/user_<id>/<filename>"""
    return f'sof_documents/user_{instance.user.id}/{filename}'

class SoFDocument(models.Model):
    FILE_TYPE = [
        ('pdf', 'PDF'),
        ('word', 'Word'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('compleated', 'Compleated'),
        ('failed', 'Failed'),
    ]

    # Primary Key and Relationships
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="sof_documents"
    )

    # File Infomation
    file = models.FileField(upload_to=user_directory_path)
    file_name = models.CharField(max_length=30, blank=True)
    file_type = models.CharField(max_length=10, choices=FILE_TYPE)

    # File Processing Status
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')

    # Time Stamps
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "SoF Document"
        verbose_name_plural = "SoF Documents"

    def __str__(self):
        return f"{self.file_name or self.file.name} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        # Set original filename and file type if not already set
        if self.file and not self.file_name :
            self.file_name = self.file_name

        # Determine file type by their extension
        if self.file and not self.file_type:
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext == '.pdf':
                self.file_type = '.pdf'
            elif ext in ['.doc', '.docx']:
                self.file_type = 'word' if ext == '.doc' else 'docx'

        super().save(*args, **kwargs)

    def get_file_size(self):
        """Return human readlable format"""
        pass


class SOFData(models.Model):

    documnent = models.OneToOneField(
        SoFDocument,
        on_delete=models.CASCADE,
        related_name = 'extracted_data'
    )
    extracted_data = models.JSONField(default=dict)
    extracted_at = models.DateTimeField(auto_now_add=True)
    confidence_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"Data from {self.documnent.file.name} by {self.documnent.user.username}"
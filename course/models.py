from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    course_files = models.ManyToManyField('File', related_name='courses', blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.name


class File(models.Model):
    course = models.ForeignKey(Course, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(
        upload_to='file_files/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx',
                    'xls', 'xlsx', 'zip', 'rar', 'jpg', 'jpeg', 'png'
                ]
            )
        ]
    )
    uploaded_by = models.ForeignKey(
        User,
        related_name='files',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name_plural = 'Files'
    
    def __str__(self):
        return self.name
    
    def get_file_size(self):
        """Return human-readable file size"""
        if self.file:
            size = self.file.size
            if size < 1024:
                return f'{size} B'
            elif size < 1024 * 1024:
                return f'{size / 1024:.2f} KB'
            else:
                return f'{size / (1024 * 1024):.2f} MB'
        return 'N/A'

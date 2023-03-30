from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.name

class File(models.Model):
    course = models.ForeignKey(Course, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='file_files/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
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
    file = models.FileField(upload_to='file_files/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, related_name='files', on_delete=models.SET_NULL, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

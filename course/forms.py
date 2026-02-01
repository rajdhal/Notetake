from django import forms
from django.core.exceptions import ValidationError

from .models import Course, File

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

# Maximum file size in bytes (50MB)
MAX_FILE_SIZE = 50 * 1024 * 1024

# Allowed file extensions
ALLOWED_EXTENSIONS = [
    'pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 
    'xls', 'xlsx', 'zip', 'rar', 'jpg', 'jpeg', 'png'
]


class NewFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('course', 'name', 'file', 'description')
        widgets = {
            'course': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'file': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4
            }),            
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        
        if file:
            # Check file size
            if file.size > MAX_FILE_SIZE:
                raise ValidationError(
                    f'File size must not exceed {MAX_FILE_SIZE // (1024 * 1024)}MB. '
                    f'Your file is {file.size // (1024 * 1024)}MB.'
                )
            
            # Check file extension
            file_extension = file.name.split('.')[-1].lower()
            if file_extension not in ALLOWED_EXTENSIONS:
                raise ValidationError(
                    f'File type ".{file_extension}" is not allowed. '
                    f'Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'
                )
        
        return file
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        # Sanitize the name to prevent path traversal
        if name:
            # Remove any path separators
            name = name.replace('/', '').replace('\\', '').strip()
            
            if not name:
                raise ValidationError('File name cannot be empty.')
        
        return name


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name:
            name = name.strip()
            
            # Check if course with this name already exists
            if Course.objects.filter(name__iexact=name).exists():
                raise ValidationError('A course with this name already exists.')
        
        return name
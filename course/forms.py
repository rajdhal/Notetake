from django import forms

from .models import Course, File

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('course', 'name', 'file', 'description')
        widgets = {
            'course':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'file':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),            
        }

class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name',)
        widgets = {
            'name':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
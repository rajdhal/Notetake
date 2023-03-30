from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, File


# Create your views here.

def file(request, pk):
    file = get_object_or_404(File, pk=pk)
    
    return render(request, 'course/file.html', {
        'file': file
    })

def course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course_files = File.objects.filter(course=course)
    return render(request, 'course/course.html', {
        'course': course,
        'course_files': course_files
    })
    

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewFileForm, NewCourseForm
from .models import Course, File
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import FileSerializer


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
    
def newFile(request):
    if request.method == 'POST':
        form = NewFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user #This is the user that is logged in, might need to remove this
            file.save()
            return redirect('course:file', pk=file.id)
        else:
            form = NewFileForm()
    form = NewFileForm()
    
    return render(request, 'course/form.html', {
        'form': form,
        'title' : 'New File',
    })

def newCourse(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course:course', pk=course.id)
        else:
            form = NewCourseForm()
    form = NewCourseForm()
    
    return render(request, 'course/form.html', {
        'form': form,
        'title' : 'Add Course',
    })

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # Additional actions if needed
    @action(detail=True, methods=['get'])
    def get_file_info(self, request, pk=None):
        file = self.get_object()
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


@login_required
def deleteFile(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return redirect('core:index')

file_list = FileViewSet.as_view({'get': 'list'})
file_detail = FileViewSet.as_view({'get': 'retrieve'})
file_create = FileViewSet.as_view({'post': 'create'})
file_update = FileViewSet.as_view({'put': 'update'})
file_delete = FileViewSet.as_view({'delete': 'destroy'})
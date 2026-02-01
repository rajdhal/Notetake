from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .forms import NewFileForm, NewCourseForm
from .models import Course, File
from .serializers import FileSerializer


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


@login_required
def newFile(request):
    if request.method == 'POST':
        form = NewFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user
            file.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('course:file', pk=file.id)
    else:
        form = NewFileForm()
    
    return render(request, 'course/form.html', {
        'form': form,
        'title': 'New File',
    })


@login_required
def newCourse(request):
    # Only staff/admin users can create courses
    if not request.user.is_staff:
        raise PermissionDenied("Only administrators can create courses.")
    
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course created successfully!')
            return redirect('course:course', pk=course.id)
    else:
        form = NewCourseForm()
    
    return render(request, 'course/form.html', {
        'form': form,
        'title': 'Add Course',
    })


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_file_info(self, request, pk=None):
        file = self.get_object()
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
    
    def perform_update(self, serializer):
        # Only allow the uploader or staff to update
        if serializer.instance.uploaded_by != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You can only edit your own files.")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Only allow the uploader or staff to delete
        if instance.uploaded_by != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You can only delete your own files.")
        instance.delete()


@login_required
def deleteFile(request, pk):
    file = get_object_or_404(File, pk=pk)
    
    # Only allow the uploader or staff to delete
    if file.uploaded_by != request.user and not request.user.is_staff:
        raise PermissionDenied("You can only delete your own files.")
    
    file.delete()
    messages.success(request, 'File deleted successfully!')
    return redirect('core:index')


# These views are no longer needed with the ViewSet, but kept for backwards compatibility
file_list = FileViewSet.as_view({'get': 'list'})
file_detail = FileViewSet.as_view({'get': 'retrieve'})
file_create = FileViewSet.as_view({'post': 'create'})
file_update = FileViewSet.as_view({'put': 'update'})
file_delete = FileViewSet.as_view({'delete': 'destroy'})
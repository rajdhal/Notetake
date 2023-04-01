from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect


from .forms import NewFileForm, NewCourseForm
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
        'course_files': course_files.order_by('-votes')
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


@login_required
def deleteFile(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return redirect('core:index')

@login_required
def upvote(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.votes += 1
    file.save()
    return redirect('course:file', pk=file.id)

@login_required
def downvote(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.votes -= 1
    file.save()
    return redirect('course:file', pk=file.id)
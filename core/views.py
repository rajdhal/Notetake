from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from course.models import Course, File
from .forms import SignUpForm

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from course.models import Course, File
from .forms import SignUpForm
import os
import mimetypes


def index(request):
    files = File.objects.all()[0:6]
    courses = Course.objects.all()
    return render(request, 'core/index.html',{
       'courses': courses,
       'files': files,
    })


@login_required
def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    
    # Security: Verify the file exists and is within the media directory
    if not file.file:
        raise Http404("File not found")
    
    file_path = file.file.path
    
    # Prevent path traversal attacks
    media_root = os.path.abspath(settings.MEDIA_ROOT)
    requested_path = os.path.abspath(file_path)
    
    if not requested_path.startswith(media_root):
        raise Http404("Invalid file path")
    
    if not os.path.exists(requested_path):
        raise Http404("File not found on disk")
    
    # Determine the content type
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'
    
    # Use FileResponse for better performance with large files
    response = FileResponse(open(requested_path, 'rb'), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file.file.name)}"'
    
    return response

def contact(request):
    return render(request, 'core/contact.html',)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('core:index')
    else:
        return render(request, 'core/login.html')


def logout(request):
    auth_logout(request)
    return redirect('core:index')
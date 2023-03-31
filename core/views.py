from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from course.models import Course, File
from .forms import SignUpForm

def index(request):
    files = File.objects.all()[0:6]
    courses = Course.objects.all()
    return render(request, 'core/index.html',{
       'courses': courses,
       'files': files,
    })

def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file_path = file.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read())
        response['Content-Disposition'] = 'attachment; filename=' + file.file.name.split('/')[-1]
        response['Content-Type'] = 'application/octet-stream'
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
        login(request, user)
        return redirect('core:index')
    else:
        return render(request, 'core/login.html')


def logout(request):
    logout(request)
    return redirect('core:index')
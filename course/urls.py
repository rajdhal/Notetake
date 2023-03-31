from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.course, name='course'),
    path('upload/', views.newFile, name='newFile'),
    path('new/', views.newCourse, name='newCourse'),
    path('<int:pk>/', views.course, name='course'),
    path('file/<int:pk>/', views.file, name='file'),
]
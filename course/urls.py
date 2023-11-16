from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from course.views import course, newFile, newCourse, file, deleteFile, FileViewSet

app_name = 'course'


urlpatterns = [
    path('', views.course, name='course'),
    path('upload/', views.newFile, name='newFile'),
    path('new/', views.newCourse, name='newCourse'),
    path('<int:pk>/', views.course, name='course'),
    path('file/<int:pk>/', views.file, name='file'),
    path('file/<int:pk>/delete/', views.deleteFile, name='deleteFile'),
]
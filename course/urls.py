from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.course, name='course'),
    path('<int:pk>/', views.course, name='course'),
    path('file/<int:pk>/', views.file, name='file'),
]

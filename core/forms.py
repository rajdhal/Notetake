from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))
    
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))
    
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))
    
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))
    
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-slate-300 rounded'}))